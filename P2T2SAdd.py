# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p2t2s-add.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_window(object):
    def setupUi(self, add_window):
        add_window.setObjectName("add_window")
        add_window.resize(1200, 650)
        add_window.setMinimumSize(QtCore.QSize(1200, 650))
        add_window.setMaximumSize(QtCore.QSize(1200, 650))
        self.centralwidget = QtWidgets.QWidget(add_window)
        self.centralwidget.setObjectName("centralwidget")
        self.topic_gb = QtWidgets.QGroupBox(self.centralwidget)
        self.topic_gb.setGeometry(QtCore.QRect(0, 9, 361, 531))
        self.topic_gb.setObjectName("topic_gb")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.topic_gb)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 20, 361, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(5, 10, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topic_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.topic_label.setObjectName("topic_label")
        self.verticalLayout_2.addWidget(self.topic_label)
        self.topic_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.topic_edit.setFont(font)
        self.topic_edit.setObjectName("topic_edit")
        self.verticalLayout_2.addWidget(self.topic_edit)
        self.cases_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cases_label.setObjectName("cases_label")
        self.verticalLayout_2.addWidget(self.cases_label)
        self.cases_edit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cases_edit.setFont(font)
        self.cases_edit.setObjectName("cases_edit")
        self.verticalLayout_2.addWidget(self.cases_edit)
        self.add_conditions_gb = QtWidgets.QGroupBox(self.centralwidget)
        self.add_conditions_gb.setGeometry(QtCore.QRect(369, 9, 831, 531))
        self.add_conditions_gb.setObjectName("add_conditions_gb")
        self.new_condition_gb = QtWidgets.QGroupBox(self.add_conditions_gb)
        self.new_condition_gb.setGeometry(QtCore.QRect(20, 40, 521, 481))
        self.new_condition_gb.setObjectName("new_condition_gb")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.new_condition_gb)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 19, 521, 461))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.new_condition_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.new_condition_label.setObjectName("new_condition_label")
        self.verticalLayout_3.addWidget(self.new_condition_label)
        self.new_condition_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_condition_edit.setFont(font)
        self.new_condition_edit.setObjectName("new_condition_edit")
        self.verticalLayout_3.addWidget(self.new_condition_edit)
        self.new_condition_ques_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.new_condition_ques_label.setObjectName("new_condition_ques_label")
        self.verticalLayout_3.addWidget(self.new_condition_ques_label)
        self.new_condition_ques_edit = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_condition_ques_edit.setFont(font)
        self.new_condition_ques_edit.setObjectName("new_condition_ques_edit")
        self.verticalLayout_3.addWidget(self.new_condition_ques_edit)
        self.add_condition_but = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.add_condition_but.setObjectName("add_condition_but")
        self.verticalLayout_3.addWidget(self.add_condition_but)
        self.added_conditions_gb = QtWidgets.QGroupBox(self.add_conditions_gb)
        self.added_conditions_gb.setGeometry(QtCore.QRect(569, 39, 261, 481))
        self.added_conditions_gb.setObjectName("added_conditions_gb")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.added_conditions_gb)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(-1, 19, 261, 461))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.added_conditions_list = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.added_conditions_list.setFont(font)
        self.added_conditions_list.setObjectName("added_conditions_list")
        self.verticalLayout_4.addWidget(self.added_conditions_list)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 550, 801, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_and_close_but = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.save_and_close_but.setObjectName("save_and_close_but")
        self.horizontalLayout.addWidget(self.save_and_close_but)
        add_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(add_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        add_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(add_window)
        self.statusbar.setObjectName("statusbar")
        add_window.setStatusBar(self.statusbar)

        self.retranslateUi(add_window)
        QtCore.QMetaObject.connectSlotsByName(add_window)

    def retranslateUi(self, add_window):
        _translate = QtCore.QCoreApplication.translate
        add_window.setWindowTitle(_translate("add_window", "P2T2S - New Topic"))
        self.topic_gb.setTitle(_translate("add_window", "Add Topic"))
        self.topic_label.setText(_translate("add_window", "Name"))
        self.cases_label.setText(_translate("add_window", "Cases"))
        self.add_conditions_gb.setTitle(_translate("add_window", "Add Conditions"))
        self.new_condition_gb.setTitle(_translate("add_window", "Add Condition"))
        self.new_condition_label.setText(_translate("add_window", "Name"))
        self.new_condition_ques_label.setText(_translate("add_window", "Questions/Clerking"))
        self.add_condition_but.setText(_translate("add_window", "Add Condition"))
        self.added_conditions_gb.setTitle(_translate("add_window", "Added Conditions"))
        self.save_and_close_but.setText(_translate("add_window", "Save And Close"))