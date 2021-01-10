import sys
from PyQt5 import QtCore, QtMultimedia, QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    filename = 'hello.mp3'
    fullpath = QtCore.QDir.current().absoluteFilePath(filename)
    url = QtCore.QUrl.fromLocalFile(fullpath)
    content = QtMultimedia.QMediaContent(url)
    player = QtMultimedia.QMediaPlayer()
    player.setMedia(content)
    player.play()
    sys.exit(app.exec_())