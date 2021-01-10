import os.path
from  PyQt5 import  QtCore, QtWidgets, QtMultimedia
from P2T2SMain import Ui_MainWindow
from AddWindow import  AddWindow
from AppController import  AppController
from gtts import gTTS
import requests


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)
        self.topic_to_study =  AppController.get_topic_to_study()
        self.main_window.topic_label.setText(self.topic_to_study.get_topic())
        self.main_window.case_edit.setText(self.topic_to_study.get_case())
        self.add_win = None
        self.conditions_list = None
        self.selected_condition = None
        self.selected_questions = None
        self.setup_signals()
        self.player = QtMultimedia.QMediaPlayer()
        self.current_audio_path = "C:/p2t2s/audios/v1/"
        self.current_audio_playlist_path = "C:/p2t2s/audios/v1/playlist/"
        self.audio_file = None
        self.msg_box = QtWidgets.QMessageBox(self)
        self.play_list = QtMultimedia.QMediaPlaylist()


    def setup_signals(self):
        self.main_window.show_next_case_but.clicked.connect(self.show_next_case)
        self.main_window.show_conditions_but.clicked.connect(self.show_conditions)
        self.main_window.read_question_but.clicked.connect(self.read_questions)
        self.main_window.conditions_list.itemClicked.connect(self.item_clicked)
        self.main_window.addAction.triggered.connect(self.open_add_window)

    def show_next_case(self):
        self.topic_to_study = AppController.get_topic_to_study()
        self.main_window.case_edit.setText(self.topic_to_study.get_case())
        self.main_window.topic_label.setText(self.topic_to_study.get_topic())

    def show_conditions(self):
        if self.topic_to_study.get_conditions_ques() is None:
            return
        self.conditions_list = [condition_questions.get_condition() for condition_questions in self.topic_to_study.get_conditions_ques()]
        self.main_window.conditions_list.clear()
        self.main_window.conditions_list.addItems(self.conditions_list)

    def item_clicked(self, selected_item):

        self.selected_condition = selected_item.text()

        for condition_questions in self.topic_to_study.get_conditions_ques():
            if self.selected_condition == condition_questions.get_condition():
                self.main_window.questions_list.clear()
                self.selected_questions = condition_questions.get_questions()
                self.main_window.questions_list.addItems(self.selected_questions)
                break

    def open_add_window(self):
        self.setVisible(False)
        self.add_win = AddWindow(self)
        self.add_win.show()


    def prepare_audios(self):
        empty_str = " "
        conditions_str = " ".join(self.conditions_list)
        question_str = f"Questions for {self.selected_condition} are - {empty_str.join(self.selected_questions)}"
        audio_string = f"Topic is {self.topic_to_study.get_topic()}... Associations are - {conditions_str}.{question_str}."
        audio_gtts = gTTS(audio_string, lang="en-ng")
        audio_gtts.save(self.audio_file)

    def does_audio_exist(self):

        self.audio_file = f"{self.current_audio_path}{self.topic_to_study.get_topic()}-{self.selected_condition}-v1.mp3"
        if os.path.isfile(self.audio_file):
            return True
        return False

    def play(self):

        url = QtCore.QUrl.fromLocalFile(self.audio_file)
        content = QtMultimedia.QMediaContent(url)

        self.player.setMedia(content)
        self.player.mediaStatusChanged.connect(self.media_status_changed)
        self.player.play()

    def media_status_changed(self, status):
        pass  # todo

    def read_questions(self):
        if not self.has_internet():
            self.show_message_box(QtWidgets.QMessageBox.Information,"No internet connection")
            return
        if self.selected_condition is None or self.selected_questions is None:
            return

        if self.does_audio_exist():
            self.play()
        else:
            self.prepare_audios()
            self.play()

    def has_internet(self):
        url='http://www.google.com/'
        try:
            r = requests.head(url, timeout=3)
            return True

        except requests.ConnectionError as ex:
            return False

    def show_message_box(self,icon, msg):

        self.msg_box.setIcon(icon)
        self.msg_box.setText(msg)
        self.msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.msg_box.exec_()

    def prepare_audio_playlist(self):
        empty_str = " "
        topic_condition_path = f"{self.current_audio_playlist_path}" \
                               f"{self.topic_to_study.get_topic()}-{self.selected_condition}-v1.mp3"
        condition_questions_path = f"{self.current_audio_playlist_path}" \
                                   f"{self.topic_to_study.get_topic()}-{self.selected_condition}-questions-v1.mp3"
        if not os.path.isfile(topic_condition_path):
            conditions_str = f"Associations for  {self.topic_to_study.get_topic()} are".join(self.conditions_list)
            conditions_gtts = gTTS(conditions_str)
            conditions_gtts.save(topic_condition_path)
        if not os.path.isfile(condition_questions_path)    :
            question_str = f"Questions for {self.selected_condition} are - {empty_str.join(self.selected_questions)}"
            questions_gtts = gTTS(question_str)
            questions_gtts.save(condition_questions_path)

        self.play_list.addMedia(QtCore.QUrl(topic_condition_path))
        self.play_list.addMedia(QtCore.QUrl(condition_questions_path))
        self.play_list.currentIndex(0)

    def play_playlist(self,playlist):
        self.player.mediaStatusChanged.connect(self.media_status_changed)
        self.player.setPlaylist(playlist)
        self.player.play()
