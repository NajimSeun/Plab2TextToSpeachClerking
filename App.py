import  sys
from PyQt5 import  QtWidgets
from AddWindow import AddWindow
from MainWindow import  MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # add_win = AddWindow()
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())