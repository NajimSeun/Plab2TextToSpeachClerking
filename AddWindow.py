from PyQt5 import QtCore, QtWidgets
from P2T2SAdd import Ui_add_window
from AppController import *

separator = "#"


class AddWindow(QtWidgets.QMainWindow):

    def __init__(self, main_window):
        super().__init__()
        self.widgets_container = Ui_add_window()
        self.widgets_container.setupUi(self)
        self.conditions_ques_list = {}
        self.setup_signals()
        self.main_window = main_window

    def setup_signals(self):

        self.widgets_container.add_condition_but.clicked.connect(self.add_condition)
        self.widgets_container.save_and_close_but.clicked.connect(self.save_and_close_widgets_container)

    def add_condition(self):
        condition = self.widgets_container.new_condition_edit.text().strip()
        condition_ques = self.widgets_container.new_condition_ques_edit.toPlainText().strip()

        if condition == "" or condition_ques == "":
            return
        condition_ques = condition_ques.replace("\n", "")
        if condition_ques.rfind(separator) == len(condition_ques) - 1:
            condition_ques = condition_ques.removesuffix(separator)
        ques_list = condition_ques.split(separator)
        self.conditions_ques_list.update({condition: ques_list})
        self.widgets_container.new_condition_edit.setText("")
        self.widgets_container.new_condition_ques_edit.setText("")
        self.widgets_container.added_conditions_list.addItem(condition)


    def save_and_close_widgets_container(self):
        topic = self.widgets_container.topic_edit.text().strip()
        cases = self.widgets_container.cases_edit.toPlainText().strip()
        if topic == "" or cases == "" or len(self.conditions_ques_list) == 0:
            return
        cases = cases.replace("\n", "")
        if cases.rfind(separator) == len(cases) - 1:
            cases = cases.removesuffix(separator)
        self.widgets_container.save_and_close_but.setEnabled(False)
        cases_list = cases.split(separator)
        AppController.add_topic(topic, cases_list, self.conditions_ques_list)


    def closeEvent(self, event):
        self.main_window.setVisible(True)
