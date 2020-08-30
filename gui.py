# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 615)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setToolTip("")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grpMain = QtWidgets.QGroupBox(self.centralwidget)
        self.grpMain.setGeometry(QtCore.QRect(0, -20, 541, 711))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.grpMain.setFont(font)
        self.grpMain.setTitle("")
        self.grpMain.setObjectName("grpMain")
        self.grpSearchResults = QtWidgets.QGroupBox(self.grpMain)
        self.grpSearchResults.setEnabled(True)
        self.grpSearchResults.setGeometry(QtCore.QRect(10, 26, 261, 401))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.grpSearchResults.setFont(font)
        self.grpSearchResults.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grpSearchResults.setObjectName("grpSearchResults")
        self.lstSkills = QtWidgets.QListWidget(self.grpSearchResults)
        self.lstSkills.setGeometry(QtCore.QRect(10, 60, 241, 271))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lstSkills.setFont(font)
        self.lstSkills.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lstSkills.setViewMode(QtWidgets.QListView.ListMode)
        self.lstSkills.setObjectName("lstSkills")
        self.txtSearch = QtWidgets.QLineEdit(self.grpSearchResults)
        self.txtSearch.setGeometry(QtCore.QRect(62, 23, 189, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtSearch.setFont(font)
        self.txtSearch.setObjectName("txtSearch")
        self.label = QtWidgets.QLabel(self.grpSearchResults)
        self.label.setGeometry(QtCore.QRect(6, 27, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnResetAll = QtWidgets.QPushButton(self.grpSearchResults)
        self.btnResetAll.setGeometry(QtCore.QRect(10, 340, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btnResetAll.setFont(font)
        self.btnResetAll.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnResetAll.setAutoDefault(True)
        self.btnResetAll.setDefault(False)
        self.btnResetAll.setFlat(False)
        self.btnResetAll.setObjectName("btnResetAll")
        self.groupBox = QtWidgets.QGroupBox(self.grpSearchResults)
        self.groupBox.setGeometry(QtCore.QRect(130, 327, 120, 64))
        self.groupBox.setObjectName("groupBox")
        self.rdbNormal = QtWidgets.QRadioButton(self.groupBox)
        self.rdbNormal.setGeometry(QtCore.QRect(26, 21, 82, 17))
        self.rdbNormal.setChecked(True)
        self.rdbNormal.setObjectName("rdbNormal")
        self.rdbModified = QtWidgets.QRadioButton(self.groupBox)
        self.rdbModified.setGeometry(QtCore.QRect(26, 40, 82, 17))
        self.rdbModified.setObjectName("rdbModified")
        self.grpSearch_2 = QtWidgets.QGroupBox(self.grpMain)
        self.grpSearch_2.setGeometry(QtCore.QRect(10, 426, 521, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.grpSearch_2.setFont(font)
        self.grpSearch_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grpSearch_2.setCheckable(False)
        self.grpSearch_2.setObjectName("grpSearch_2")
        self.btnApply = QtWidgets.QPushButton(self.grpSearch_2)
        self.btnApply.setGeometry(QtCore.QRect(10, 30, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btnApply.setFont(font)
        self.btnApply.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnApply.setAutoDefault(True)
        self.btnApply.setDefault(True)
        self.btnApply.setFlat(False)
        self.btnApply.setObjectName("btnApply")
        self.btnRun = QtWidgets.QPushButton(self.grpSearch_2)
        self.btnRun.setGeometry(QtCore.QRect(270, 30, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btnRun.setFont(font)
        self.btnRun.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnRun.setAutoDefault(True)
        self.btnRun.setDefault(False)
        self.btnRun.setFlat(False)
        self.btnRun.setObjectName("btnRun")
        self.btnSaveProfile = QtWidgets.QPushButton(self.grpSearch_2)
        self.btnSaveProfile.setGeometry(QtCore.QRect(10, 80, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btnSaveProfile.setFont(font)
        self.btnSaveProfile.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnSaveProfile.setAutoDefault(True)
        self.btnSaveProfile.setDefault(False)
        self.btnSaveProfile.setFlat(False)
        self.btnSaveProfile.setObjectName("btnSaveProfile")
        self.btnLoadProfile = QtWidgets.QPushButton(self.grpSearch_2)
        self.btnLoadProfile.setGeometry(QtCore.QRect(270, 80, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btnLoadProfile.setFont(font)
        self.btnLoadProfile.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnLoadProfile.setAutoDefault(True)
        self.btnLoadProfile.setDefault(False)
        self.btnLoadProfile.setFlat(False)
        self.btnLoadProfile.setObjectName("btnLoadProfile")
        self.btnAddContextMenu = QtWidgets.QPushButton(self.grpSearch_2)
        self.btnAddContextMenu.setGeometry(QtCore.QRect(10, 130, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btnAddContextMenu.setFont(font)
        self.btnAddContextMenu.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnAddContextMenu.setAutoDefault(True)
        self.btnAddContextMenu.setDefault(False)
        self.btnAddContextMenu.setFlat(False)
        self.btnAddContextMenu.setObjectName("btnAddContextMenu")
        self.btnRestoreDataPak = QtWidgets.QPushButton(self.grpSearch_2)
        self.btnRestoreDataPak.setGeometry(QtCore.QRect(270, 130, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btnRestoreDataPak.setFont(font)
        self.btnRestoreDataPak.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnRestoreDataPak.setAutoDefault(True)
        self.btnRestoreDataPak.setDefault(False)
        self.btnRestoreDataPak.setFlat(False)
        self.btnRestoreDataPak.setObjectName("btnRestoreDataPak")
        self.grpSearchResults_2 = QtWidgets.QGroupBox(self.grpMain)
        self.grpSearchResults_2.setEnabled(True)
        self.grpSearchResults_2.setGeometry(QtCore.QRect(280, 26, 251, 401))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.grpSearchResults_2.setFont(font)
        self.grpSearchResults_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grpSearchResults_2.setObjectName("grpSearchResults_2")
        self.grpSearch_6 = QtWidgets.QGroupBox(self.grpSearchResults_2)
        self.grpSearch_6.setGeometry(QtCore.QRect(10, 180, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.grpSearch_6.setFont(font)
        self.grpSearch_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grpSearch_6.setCheckable(False)
        self.grpSearch_6.setObjectName("grpSearch_6")
        self.lblValueNew = QtWidgets.QLabel(self.grpSearch_6)
        self.lblValueNew.setGeometry(QtCore.QRect(10, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblValueNew.setFont(font)
        self.lblValueNew.setText("")
        self.lblValueNew.setAlignment(QtCore.Qt.AlignCenter)
        self.lblValueNew.setObjectName("lblValueNew")
        self.grpSearch_3 = QtWidgets.QGroupBox(self.grpSearchResults_2)
        self.grpSearch_3.setGeometry(QtCore.QRect(10, 20, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.grpSearch_3.setFont(font)
        self.grpSearch_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grpSearch_3.setCheckable(False)
        self.grpSearch_3.setObjectName("grpSearch_3")
        self.lblValueName = QtWidgets.QLabel(self.grpSearch_3)
        self.lblValueName.setGeometry(QtCore.QRect(10, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblValueName.setFont(font)
        self.lblValueName.setText("")
        self.lblValueName.setIndent(-1)
        self.lblValueName.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.lblValueName.setObjectName("lblValueName")
        self.grpSearch_4 = QtWidgets.QGroupBox(self.grpSearchResults_2)
        self.grpSearch_4.setGeometry(QtCore.QRect(10, 100, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.grpSearch_4.setFont(font)
        self.grpSearch_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grpSearch_4.setCheckable(False)
        self.grpSearch_4.setObjectName("grpSearch_4")
        self.lblValueOriginal = QtWidgets.QLabel(self.grpSearch_4)
        self.lblValueOriginal.setGeometry(QtCore.QRect(10, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblValueOriginal.setFont(font)
        self.lblValueOriginal.setText("")
        self.lblValueOriginal.setAlignment(QtCore.Qt.AlignCenter)
        self.lblValueOriginal.setObjectName("lblValueOriginal")
        self.grpSearch_5 = QtWidgets.QGroupBox(self.grpSearchResults_2)
        self.grpSearch_5.setGeometry(QtCore.QRect(10, 260, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.grpSearch_5.setFont(font)
        self.grpSearch_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.grpSearch_5.setCheckable(False)
        self.grpSearch_5.setObjectName("grpSearch_5")
        self.txtSetValue = QtWidgets.QLineEdit(self.grpSearch_5)
        self.txtSetValue.setGeometry(QtCore.QRect(10, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txtSetValue.setFont(font)
        self.txtSetValue.setInputMask("")
        self.txtSetValue.setText("")
        self.txtSetValue.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSetValue.setObjectName("txtSetValue")
        self.btnChange = QtWidgets.QPushButton(self.grpSearchResults_2)
        self.btnChange.setGeometry(QtCore.QRect(10, 340, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btnChange.setFont(font)
        self.btnChange.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnChange.setAutoDefault(True)
        self.btnChange.setDefault(False)
        self.btnChange.setFlat(False)
        self.btnChange.setObjectName("btnChange")
        self.btnReset = QtWidgets.QPushButton(self.grpSearchResults_2)
        self.btnReset.setGeometry(QtCore.QRect(130, 340, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.btnReset.setFont(font)
        self.btnReset.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnReset.setAutoDefault(True)
        self.btnReset.setDefault(False)
        self.btnReset.setFlat(False)
        self.btnReset.setObjectName("btnReset")
        self.lblLog = QtWidgets.QLabel(self.grpMain)
        self.lblLog.setGeometry(QtCore.QRect(10, 611, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblLog.setFont(font)
        self.lblLog.setText("")
        self.lblLog.setObjectName("lblLog")
        self.btnCredits = QtWidgets.QPushButton(self.grpMain)
        self.btnCredits.setGeometry(QtCore.QRect(440, 610, 51, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCredits.sizePolicy().hasHeightForWidth())
        self.btnCredits.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setKerning(False)
        self.btnCredits.setFont(font)
        self.btnCredits.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnCredits.setAutoDefault(False)
        self.btnCredits.setDefault(False)
        self.btnCredits.setFlat(False)
        self.btnCredits.setObjectName("btnCredits")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dying Light Skill Editor (DLSE)"))
        self.grpSearchResults.setTitle(_translate("MainWindow", "Skills"))
        self.label.setText(_translate("MainWindow", "Search"))
        self.btnResetAll.setText(_translate("MainWindow", "Reset All"))
        self.groupBox.setTitle(_translate("MainWindow", "Sort"))
        self.rdbNormal.setText(_translate("MainWindow", "Normal"))
        self.rdbModified.setText(_translate("MainWindow", "Modified"))
        self.grpSearch_2.setTitle(_translate("MainWindow", "Output"))
        self.btnApply.setText(_translate("MainWindow", "Apply"))
        self.btnRun.setText(_translate("MainWindow", "Run"))
        self.btnSaveProfile.setText(_translate("MainWindow", "Save Profile"))
        self.btnLoadProfile.setText(_translate("MainWindow", "Load Profile"))
        self.btnAddContextMenu.setText(_translate("MainWindow", "Add DLSE to Context Menu"))
        self.btnRestoreDataPak.setText(_translate("MainWindow", "Restore Backup"))
        self.grpSearchResults_2.setTitle(_translate("MainWindow", "Details"))
        self.grpSearch_6.setTitle(_translate("MainWindow", "New Value"))
        self.grpSearch_3.setTitle(_translate("MainWindow", "Name"))
        self.grpSearch_4.setTitle(_translate("MainWindow", "Original Value"))
        self.grpSearch_5.setTitle(_translate("MainWindow", "Set Value"))
        self.btnChange.setText(_translate("MainWindow", "Change"))
        self.btnReset.setText(_translate("MainWindow", "Reset"))
        self.btnCredits.setText(_translate("MainWindow", "Credits"))
