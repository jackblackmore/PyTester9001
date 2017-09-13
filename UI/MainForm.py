# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyTester9001(object):
    def setupUi(self, PyTester9001):
        PyTester9001.setObjectName("PyTester9001")
        PyTester9001.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(PyTester9001)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.controlButtonLayout = QtWidgets.QHBoxLayout()
        self.controlButtonLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.controlButtonLayout.setObjectName("controlButtonLayout")
        self.selectDatabaseButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectDatabaseButton.sizePolicy().hasHeightForWidth())
        self.selectDatabaseButton.setSizePolicy(sizePolicy)
        self.selectDatabaseButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.selectDatabaseButton.setObjectName("selectDatabaseButton")
        self.controlButtonLayout.addWidget(self.selectDatabaseButton)
        self.startQuizButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startQuizButton.sizePolicy().hasHeightForWidth())
        self.startQuizButton.setSizePolicy(sizePolicy)
        self.startQuizButton.setObjectName("startQuizButton")
        self.controlButtonLayout.addWidget(self.startQuizButton)
        self.gridLayout.addLayout(self.controlButtonLayout, 0, 0, 1, 1)
        self.answerLayout = QtWidgets.QVBoxLayout()
        self.answerLayout.setObjectName("answerLayout")
        self.answerLabel = QtWidgets.QLabel(self.centralwidget)
        self.answerLabel.setObjectName("answerLabel")
        self.answerLayout.addWidget(self.answerLabel)
        self.answerText = QtWidgets.QTextBrowser(self.centralwidget)
        self.answerText.setObjectName("answerText")
        self.answerLayout.addWidget(self.answerText)
        self.gridLayout.addLayout(self.answerLayout, 3, 1, 1, 1)
        self.questionLayout = QtWidgets.QVBoxLayout()
        self.questionLayout.setObjectName("questionLayout")
        self.questionLabel = QtWidgets.QLabel(self.centralwidget)
        self.questionLabel.setObjectName("questionLabel")
        self.questionLayout.addWidget(self.questionLabel)
        self.questionText = QtWidgets.QTextBrowser(self.centralwidget)
        self.questionText.setObjectName("questionText")
        self.questionLayout.addWidget(self.questionText)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.revealAnswerButton = QtWidgets.QPushButton(self.centralwidget)
        self.revealAnswerButton.setMinimumSize(QtCore.QSize(0, 70))
        self.revealAnswerButton.setObjectName("revealAnswerButton")
        self.horizontalLayout_3.addWidget(self.revealAnswerButton)
        self.answerCorrectButton = QtWidgets.QPushButton(self.centralwidget)
        self.answerCorrectButton.setMinimumSize(QtCore.QSize(0, 70))
        self.answerCorrectButton.setAutoFillBackground(False)
        self.answerCorrectButton.setStyleSheet("background-color:rgb(81, 200, 120)")
        self.answerCorrectButton.setObjectName("answerCorrectButton")
        self.horizontalLayout_3.addWidget(self.answerCorrectButton)
        self.answerIncorrectButton = QtWidgets.QPushButton(self.centralwidget)
        self.answerIncorrectButton.setMinimumSize(QtCore.QSize(0, 70))
        self.answerIncorrectButton.setStyleSheet("background-color: rgb(200, 106, 112)")
        self.answerIncorrectButton.setObjectName("answerIncorrectButton")
        self.horizontalLayout_3.addWidget(self.answerIncorrectButton)
        self.stopQuizButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopQuizButton.setMinimumSize(QtCore.QSize(0, 70))
        self.stopQuizButton.setObjectName("stopQuizButton")
        self.horizontalLayout_3.addWidget(self.stopQuizButton)
        self.questionLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.questionLayout, 3, 0, 1, 1)
        self.selectorLayout = QtWidgets.QFormLayout()
        self.selectorLayout.setObjectName("selectorLayout")
        self.moduleLabel = QtWidgets.QLabel(self.centralwidget)
        self.moduleLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.moduleLabel.setObjectName("moduleLabel")
        self.selectorLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.moduleLabel)
        self.moduleComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.moduleComboBox.setObjectName("moduleComboBox")
        self.selectorLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.moduleComboBox)
        self.partLabel = QtWidgets.QLabel(self.centralwidget)
        self.partLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.partLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.partLabel.setObjectName("partLabel")
        self.selectorLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.partLabel)
        self.partComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.partComboBox.setObjectName("partComboBox")
        self.selectorLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.partComboBox)
        self.chapterLabel = QtWidgets.QLabel(self.centralwidget)
        self.chapterLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chapterLabel.setObjectName("chapterLabel")
        self.selectorLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.chapterLabel)
        self.chapterComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.chapterComboBox.setObjectName("chapterComboBox")
        self.selectorLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.chapterComboBox)
        self.gridLayout.addLayout(self.selectorLayout, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.numberOfQuestionsSelectionLabel = QtWidgets.QLabel(self.centralwidget)
        self.numberOfQuestionsSelectionLabel.setObjectName("numberOfQuestionsSelectionLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numberOfQuestionsSelectionLabel)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 2, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        PyTester9001.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyTester9001)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        PyTester9001.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PyTester9001)
        self.statusbar.setObjectName("statusbar")
        PyTester9001.setStatusBar(self.statusbar)
        self.answerLabel.setBuddy(self.answerText)
        self.questionLabel.setBuddy(self.questionText)
        self.moduleLabel.setBuddy(self.moduleComboBox)
        self.partLabel.setBuddy(self.partComboBox)
        self.chapterLabel.setBuddy(self.chapterComboBox)

        self.retranslateUi(PyTester9001)
        QtCore.QMetaObject.connectSlotsByName(PyTester9001)

    def retranslateUi(self, PyTester9001):
        _translate = QtCore.QCoreApplication.translate
        PyTester9001.setWindowTitle(_translate("PyTester9001", "MainWindow"))
        self.selectDatabaseButton.setText(_translate("PyTester9001", "Select Database"))
        self.startQuizButton.setText(_translate("PyTester9001", "Start Quiz"))
        self.answerLabel.setText(_translate("PyTester9001", "Answer:"))
        self.questionLabel.setText(_translate("PyTester9001", "Question:"))
        self.revealAnswerButton.setText(_translate("PyTester9001", "Reveal Answer"))
        self.answerCorrectButton.setText(_translate("PyTester9001", "Correct"))
        self.answerIncorrectButton.setText(_translate("PyTester9001", "Incorrect"))
        self.stopQuizButton.setText(_translate("PyTester9001", "Stop Quiz"))
        self.moduleLabel.setText(_translate("PyTester9001", "Module: "))
        self.partLabel.setText(_translate("PyTester9001", "Part:"))
        self.chapterLabel.setText(_translate("PyTester9001", "Chapter:"))
        self.label.setText(_translate("PyTester9001", "Number of Questions in Selection: "))
        self.numberOfQuestionsSelectionLabel.setText(_translate("PyTester9001", "0"))

