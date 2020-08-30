import os, sys, webbrowser, time, qdarkstyle, shutil, ctypes

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, \
                            QApplication, \
                            QListWidgetItem, \
                            QFileDialog, \
                            QMessageBox

from dlse_credits import MySubForm
from regsitery import register_context_menu
from icon import icon_data
from gui import Ui_MainWindow
from skilledit import Editor
from paktools import copy_pak_from_game, \
                     copy_pak_to_game, \
                     extract_skills_file, \
                     update_pak

ope = os.path.exists

def clickable(widget):
    class Filter(QtCore.QObject):
        clicked = QtCore.pyqtSignal()
        def eventFilter(self, obj, event):
            if obj == widget:
                mbr = QtCore.QEvent.MouseButtonRelease
                if event.type() == mbr:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

# self.e         =      self.editor
# self.e_b       =      self.editor_backup
# self.ek        =      self.editor_k
# self.ek_b      =      self.editor_k_backup
# self.cur       =      self.current
# self.org       =      self.original
# self.sld       =      self.selected

class MyForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        
        self.w = MySubForm()
        self.version = 1.1
        
        self.exe_path = os.getcwd() + '\\DLSE.exe'
        self.PakPath = ''
        self.all_skills = []
        self.edited_skills = {}
        self.settings = {}
        
        self.cur, self.org,self.sld = [0] * 3
        
        self.e, self.eb = None, None
        self.ek, self.ekb = None, None

        # Setup UI
        self.setWindowIcon(self.processIcon())
        self.setStyleSheet(qdarkstyle.load_stylesheet())
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowTitle(f'{self.windowTitle()} v{self.version}')
        
        # Connect Controls
        ## Skill Group
        self.txtSearch.textChanged.connect(self.SearchSkills)
        self.lstSkills.itemClicked.connect(self.ShowData)
        self.btnResetAll.clicked.connect(self.ResetAllSkill)
        self.rdbNormal.toggled.connect(self.SortSkills)
        
        ## Details Group
        self.btnChange.clicked.connect(self.ChangeSkill)
        self.btnReset.clicked.connect(self.ResetSkill)
        self.btnChange.setEnabled(False)
        self.btnReset.setEnabled(False)
        # Only accept certain input according to regular pattern
        rx = QtCore.QRegExp(r"^(?=.)([+-]?([0-9]*)(\.([0-9]+))?)$")
        validator = QtGui.QRegExpValidator(
                                            rx,
                                            self
                                            )
        self.txtSetValue.setValidator(validator)
        
        ## Output Group
        self.btnApply.clicked.connect(self.ApplyChanges)
        self.btnRun.clicked.connect(self.RunGame)
        self.btnSaveProfile.clicked.connect(self.SaveProfile)
        self.btnLoadProfile.clicked.connect(self.LoadProfile)
        self.btnAddContextMenu.clicked.connect(self.AddToContextMenu)
        self.btnRestoreDataPak.clicked.connect(self.RestoreBackup)

        ## Credits labels
        self.btnCredits.clicked.connect(self.ShowCredits)
        #clickable(self.lblPatreon).connect(self.patreon_clicked)
        #self.lblPatreon.setText("<font color='#f96854'>Patreon</font>")


    def ShowCredits(self):
        self.w.show()
        self.w.showPatrons()
        self.w.get_mod_stats()

    def run(self):
        QApplication.processEvents()

    def process_arg_from_context_menu(self):
        args = sys.argv
        if len(args) > 1:
            self.LoadProfile(args[1])
    
    # Create icon from raw data in icon.py
    def processIcon(self):
        pix = QtGui.QPixmap()
        pix.loadFromData(icon_data)
        icon = QtGui.QIcon()
        icon.addPixmap(pix)
        return icon

    def Logger(self, text, color):
        if len(text) > 70:
            text = text[:70] + '...'
        self.lblLog.setText(f"<font color='{color}'>{text}</font>")
    
    def Color(self, item, colors):
        elmnt = QListWidgetItem(item)
        elmnt.setBackground(QtGui.QColor(colors[0]))
        elmnt.setForeground(QtGui.QColor(colors[1]))
        return elmnt
    
    def CleanAndScroll(self):
        self.lstSkills.scrollToTop()
        self.btnChange.setEnabled(False)
        self.btnReset.setEnabled(False)
        self.lblValueName.setText('')
        self.lblValueOriginal.setText('')
        self.lblValueNew.setText('')
        self.txtSetValue.setText('')
        self.ShowSkills()
    
    def setup_app_dir(self):
        path = os.path.join(
                    os.environ['USERPROFILE'],
                    'Documents\\DLSE\\'
                    )

        # Check for app dir
        if not ope(path):
            os.mkdir(path)
        
        # Check for settings file
        if not ope(path + 'settings.cfg'):
            open(path + 'settings.cfg', 'w').write('{}')

        os.chdir(path)
        
        # Check for any errors in settings file
        try:
            self.settings = eval(open('settings.cfg', 'r').read())
            if not 'path' in self.settings:
                self.settings['path'] = ''
        except:
            self.settings = {}
        
        # Check for correct game path
        if not self.settings or not ope(self.settings['path']):
            p = self.open_dialog_box(
                'Select Dying Light executble...',
                'Excutable Files (*.exe)'
                )
            while not 'DyingLightGame.exe' in p:
                p = self.open_dialog_box(
                    'Select Dying Light executble...',
                    'Excutable Files (*.exe)'
                    )
            self.settings['path'] = p
            self.update_setting()
        
        self.load()
        self.ShowSkills()
    
    def update_setting(self):
        with open('settings.cfg', 'w') as cfg:
            cfg.write(str(self.settings))

    def open_dialog_box(self, hint, fltr, t='open'):
        desktop = os.path.join(
            os.environ['USERPROFILE'],
            'Desktop'
            )
        
        if t == 'open':
            fileName, _ = QFileDialog.getOpenFileName(
                                            self,
                                            hint,
                                            desktop,
                                            fltr
                                            )
        else:
            fileName, _ = QFileDialog.getSaveFileName(
                                            self,
                                            hint,
                                            desktop,
                                            fltr
                                            )
        return fileName

    def load(self):
        
        self.PakPath = os.path.dirname(self.settings['path'])
        
        if not ope('default_levels.xml') \
            or \
           not ope('default_levels_kiosk.xml'):
            # Get copy of pak file and create backup
            copy_pak_from_game(self.PakPath)
            shutil.copy2(
                'Data0.pak',
                'Data0_backup.pak'
                )
            
            # Extract skills xml files
            extract_skills_file(
                'default_levels',
                'default_levels_kiosk'
                )
        
            # Original file backup
            shutil.copyfile(
                'default_levels.xml',
                'default_levels_backup.xml'
                )
            shutil.copyfile(
                'default_levels_kiosk.xml',
                'default_levels_kiosk_backup.xml'
                )
        
        # Setup Editors
        for editor, name in [
                ('self.e', 'default_levels.xml'),
                ('self.ek', 'default_levels_kiosk.xml'),
                ('self.eb', 'default_levels_backup.xml'),
                ('self.ekb', 'default_levels_kiosk_backup.xml')
                ]:
            exec(f'{editor} = Editor("{name}")')
            exec(f'{editor}.load()')

        # Load skills from both default and default kiosk
        self.all_skills += list(
                                set(
                                    list(self.e.props) \
                                  + list(self.ek.props)
                                  )
                                )
        self.SortSkills()

    # Make modified skills green colored
    def SkillColor(self, skill):
        e, v = None, None
        if skill in self.e.props:
            e, v = self.e.props[skill], self.eb.props[skill]
        else:
            e, v = self.ek.props[skill], self.ekb.props[skill]

        if e[0] != v[0]:
            self.edited_skills[skill] = 0
            skill = self.Color(
                            skill,
                            ['#00ff00', '#000000']
                            )
            
        self.lstSkills.addItem(skill)

    # Sort skills by modification via radio buttons
    def SortSkills(self):
        self.lstSkills.scrollToTop()

        state = self.rdbNormal.isChecked()
        self.all_skills = sorted(self.all_skills)
        
        if state:
            self.ShowSkills()
            self.Logger(
                'IDLE',
                'white'
                )
            return
        
        for skill in self.all_skills[::-1]:
            e, v = None, None
            if skill in self.e.props:
                e, v = self.e.props[skill], self.eb.props[skill]
            else:
                e, v = self.ek.props[skill], self.ekb.props[skill]

            if e[0] != v[0]:
               self.all_skills.insert(
                   0,
                   self.all_skills.pop(
                       self.all_skills.index(skill)
                       )
                    )
        
        self.CleanAndScroll()
        
        self.Logger(
            f'{len(self.edited_skills)} skills are modified.',
            'aqua'
            )

    # Show skills in QListView
    def ShowSkills(self):
        self.lstSkills.clear()
        for skill in self.all_skills:
            self.SkillColor(skill)

    # Search skills sorted by search index
    def SearchSkills(self):
        self.lstSkills.clear()
        query = self.txtSearch.text().lower()
        filtered = [i for i in self.all_skills if query in i.lower()]
        # Filter by find index for ease if use
        sort_filtr = sorted(
            filtered,
            key=lambda i: i.lower().find(query)
            )
        if not query:
            self.ShowSkills()
        else:
            for skill in sort_filtr:
                self.SkillColor(skill)
            self.Logger(
                f'Found {len(sort_filtr)} skills.',
                'aqua'
                )

    # Show info of selected skills
    def ShowData(self):
        self.btnChange.setEnabled(True)
        self.btnReset.setEnabled(True)
        
        try:
            self.sld = self.lstSkills.currentItem().text()
        except:
            if not self.sld:
                self.sld = self.all_skills[0]

        if self.sld in self.e.props:
            self.cur = self.e.props[self.sld][0]
            self.org = self.eb.props[self.sld][0]
        elif self.sld in self.e.props and self.sld in self.ek.props:
            self.cur = self.e.props[self.sld][0]
            self.org = self.eb.props[self.sld][0]
        else:
            self.cur = self.ek.props[self.sld][0]
            self.org = self.ekb.props[self.sld][0]
        
        self.lblValueName.setText(self.sld)
        self.lblValueOriginal.setText(str(self.org))
        self.lblValueNew.setText(str(self.cur))
        self.txtSetValue.setText(str(self.cur))

    # Change skill values
    def ChangeSkill(self):        
        new_val = self.txtSetValue.text()
        
        if self.sld in self.e.props:
            self.e.edit_prop(
                self.sld,
                new_val
                )
        if self.sld in self.ek.props:
            self.ek.edit_prop(
                self.sld,
                new_val
                )
        
        self.e.update()
        self.ek.update()
        self.ShowData()
        self.SearchSkills()
        
        self.Logger(
            f'Skill {self.sld} changed to {new_val}',
            'aqua'
            )

    # Reset skill values
    def ResetSkill(self):
        if self.sld in self.e.props:
            self.e.edit_prop(
                self.sld,
                self.org
                )
        if self.sld in self.ek.props:
            self.ek.edit_prop(
                self.sld,
                self.org
                )

        if self.sld in self.edited_skills:
            self.edited_skills.pop(self.sld)
        
        self.e.update()
        self.ek.update()
        self.ShowData()
        self.SearchSkills()
        
        self.Logger(
            f'Skill {self.sld} changed to {self.org}',
            'aqua'
            )
    
    # Reset all skills in one click
    def ResetAllSkill(self):
        self.lstSkills.scrollToTop()

        for skill in self.all_skills:
            if skill in self.e.props:
                origin = self.eb.props[skill][0]
                self.e.edit_prop(
                    skill,
                    origin
                    )
            if skill in self.ek.props:
                origin = self.ekb.props[skill][0]
                self.ek.edit_prop(
                    skill,
                    origin
                    )
            if skill in self.ek.props and skill in self.e.props:
                origin = self.eb.props[skill][0]
                self.ek.edit_prop(
                    skill,
                    origin
                    )
        
        self.rdbNormal.setChecked(True)
        self.edited_skills = {}
        
        self.e.update()
        self.ek.update()
        self.ShowData()
        
        self.CleanAndScroll()
        
        self.Logger(
            'All skills were reset to original values.',
            'aqua'
            )

    # Apply changes to Data0.pak and move it to Game folder
    def ApplyChanges(self):
        st = time.time()
        
        self.grpMain.setEnabled(False);                  self.run()
        self.Logger('Updating pak file...', 'aqua');     self.run()
        update_pak(
            'default_levels',
            'default_levels_kiosk'
            );                                           self.run()
        self.Logger(
            'Copying data to game folder...',
            'aqua'
            );                                           self.run()
        copy_pak_to_game(self.PakPath);                  self.run()
        self.grpMain.setEnabled(True);                   self.run()
        
        et = int(time.time() - st)
        
        self.Logger(
            f'Skills applied successfully in {et} seconds.',
            'lime'
            )
    
    # Run the Game
    def RunGame(self):
        os.system(f'start "" "{self.settings["path"]}"')

    # Export 
    def SaveProfile(self):
        path = self.open_dialog_box(
                    'Select where to save your profile...',
                    'DLSE Files (*.dlse)',
                    t='save'
                    )

        if not path:
            self.Logger(
                'Saving operation cancelled.',
                'red'
                )
            return
        
        Saved = {
            'editor': self.e.props,
            'editor_k': self.ek.props
            }
        
        with open(path, 'w') as dlse:
            dlse.write(str(Saved))
        
        self.Logger(f'Profile {os.path.basename(path)} '
                    f'saved at {os.path.dirname(path)}.',
                    'lime'
                    )

    # Loads custom profile with edited skills
    def LoadProfile(self, custom_path=''):
        path = ''

        if not custom_path:
            path = self.open_dialog_box(
                        'Select where to import a profile...',
                        'DLSE Files (*.dlse)'
                        )
            
            if not os.path.isfile(path):
                self.Logger(
                    'No profile chosen.',
                    'red'
                    )
                return
        else:
            path = custom_path
        
        try:
            eval(open(path, 'r').read())
        except:
            self.Logger(
                'Corrupted profile.',
                'red'
                )
            return

        Saved = eval(open(path, 'r').read())
        
        # Avoid incorrect profiles
        if type(Saved) != dict or (
                            list(Saved['editor']) != list(self.e.props) \
                            or \
                            list(Saved['editor_k']) != list(self.ek.props)
                            ):
            self.Logger(
                'This profile is not supported.',
                'red'
                )
            return
        
        self.ResetAllSkill()
        
        self.e.props = Saved['editor']
        self.ek.props = Saved['editor_k']

        for skill in self.e.props:
            self.e.props[skill][1] = self.eb.props[skill][1]
        for skill in self.ek.props:
            self.ek.props[skill][1] = self.ekb.props[skill][1]
        
        self.e.update()
        self.ek.update()
        self.rdbModified.setChecked(True)
        self.SortSkills()
        
        self.CleanAndScroll()
        
        self.Logger(f'Profile {os.path.basename(path)} loaded. '
                    f'({len(self.edited_skills)} skills are modified)',
                    'lime'
                    )
    
    # Register exe to context menu
    def AddToContextMenu(self):
        if ctypes.windll.shell32.IsUserAnAdmin() != 0:
            register_context_menu(self.exe_path)
            
            # Kill explorer and start new process to refresh icon cache
            os.system('taskkill /f /im explorer.exe')
            os.system('regedit.exe /S dlse.reg')
            os.system('explorer.exe')
            
            self.Logger(
                'DLSE added to context menu.',
                'lime'
                )
        else:
            self.Logger(
                'Must run DLSE as Adminstrator',
                'red'
                )

    # Restore original Data0.pak
    def RestoreBackup(self):
        MsgBox = QMessageBox
        msgText = 'All skills will be reset to it\'s original values' \
                  '\nProceed to restore?'
        buttonReply = MsgBox.question(
                                    self,
                                    'Restore Backup',
                                    msgText,
                                    MsgBox.Yes | MsgBox.No,
                                    MsgBox.Yes
                                    )
        if buttonReply == MsgBox.No:
            self.Logger(
                    'Backup restoration cancelled.',
                    'aqua'
                    )
            return
        
        pak_path = os.path.join(
                                os.path.dirname(self.settings['path']),
                                'DW',
                                'Data0.pak'
                                )
        
        self.grpMain.setEnabled(False)
        
        self.Logger(
            'Restoring backup to game folder...',
            'aqua'
            )
        self.run()
        
        shutil.copy2(
            'Data0_backup.pak',
            pak_path
        )
        
        self.Logger(
            'Backup restored successfully',
            'lime'
            )
        
        self.grpMain.setEnabled(True)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    w = MyForm()
    w.show()
    w.setup_app_dir()
    w.process_arg_from_context_menu()

    sys.exit(app.exec_())