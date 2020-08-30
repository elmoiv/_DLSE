import webbrowser, qdarkstyle, sys, requests, re
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from icon import icon_data
from subgui import Ui_SubMainWindow

from threading import Thread

class MySubForm(QMainWindow, Ui_SubMainWindow):

    def __init__(self):
        super().__init__()

        # Setup UI
        self.setWindowIcon(self.processIcon())
        self.setStyleSheet(qdarkstyle.load_stylesheet())
        self.setupUi(self)
        self.setFixedSize(self.size())
        
        self.grpCredits.setStyleSheet('QGroupBox:title {subcontrol-position: top center;}')
        self.grpPatrons.setStyleSheet('QGroupBox:title {subcontrol-position: top center;}')
        self.grpStatics.setStyleSheet('QGroupBox:title {subcontrol-position: top center;}')
        self.grpUDL.setStyleSheet('QGroupBox:title {subcontrol-position: top center;}')
        self.grpTDL.setStyleSheet('QGroupBox:title {subcontrol-position: top center;}')
        
        # Connect Controls
        ## Credits Group
        self.btnTwitter.clicked.connect(self.Twitter)
        self.btnGitHub.clicked.connect(self.GitHub)
        self.btnPatreon.clicked.connect(self.Patreon)
        self.btnNexus.clicked.connect(self.Nexus)
        self.btnPatreon.setStyleSheet("QPushButton"
                             "{"
                             "background-color : #f96854;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #b54b3e;"
                             "}")
        self.btnNexus.setStyleSheet("QPushButton"
                             "{"
                             "background-color : #f39f2f;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #c27f27;"
                             "}")
        self.btnTwitter.setStyleSheet("QPushButton"
                             "{"
                             "background-color : #1c9deb;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #1574ad;"
                             "}")
        self.btnGitHub.setStyleSheet("QPushButton"
                             "{"
                             "background-color : #24292e;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #191f29;"
                             "}")

    def Twitter(self):
        webbrowser.open('https://twitter.com/___xpy___')

    def GitHub(self):
        webbrowser.open('https://github.com/elmoiv')

    def Patreon(self):
        webbrowser.open('https://www.patreon.com/elmoiv')
    
    def Nexus(self):
        webbrowser.open('https://www.nexusmods.com/dyinglight/users/54739042?tab=user+files')

    def get_mod_stats(self):
        Thread(target=_get_mod_stats, args=[self.lblTDL, self.lblUDL]).start()

    def showPatrons(self):
        Thread(target=_showPatrons, args=[self.lstPatrons]).start()

    # Create icon from raw data in icon.py
    def processIcon(self):
        pix = QtGui.QPixmap()
        pix.loadFromData(icon_data)
        icon = QtGui.QIcon()
        icon.addPixmap(pix)
        return icon

def _showPatrons(qlst):
    qlst.clear()
    qlst.addItem('Getting Patrons...')
    
    try:
        patrons_data = requests.get('https://raw.githubusercontent.com/elmoiv/DLSE/master/.github/patrons.txt')

        if patrons_data.status_code != 200:
            qlst.clear()
            qlst.addItem('No internet connection')
            return
    except:
        pass
    
    qlst.clear()
    for patron in patrons_data.text.split('\n'):
        if patron:
            ql = QListWidgetItem()
            ql.setText(patron)
            ql.setTextAlignment(QtCore.Qt.AlignCenter)
            qlst.addItem(ql)

def _get_mod_stats(lblt, lblu):
        lblt.setText('--')
        lblu.setText('--')
        
        try:
            # Get all mods stats for Dying Light (id = 793)
            stats = requests.get('https://staticstats.nexusmods.com/live_download_counts/mods/793.csv')

            if stats.status_code != 200:
                lblt.setText('\\(0_0)/')
                lblu.setText('\\(0_0)/')

            # Extract values via re as a dictionary
            # Key: Mod id
            # Value: [Unique DLs, Total DLs]
            stats_dct = {i[0]: i[1:] for i in re.findall(r'(\d+),(\d+),(\d+)', stats.text)}

            # My mod "DLSE" id = 491
            u, t = stats_dct['491']
            
            lblt.setText(u)
            lblu.setText(t)
        except:
            pass