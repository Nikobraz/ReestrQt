#!-*-coding:utf-8-*-
import sys
import init
# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic

( Ui_MainWindow, QMainWindow ) = uic.loadUiType('mainform.ui')


class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def __del__(self):
        self.ui = None

    def searchslot(self):
        self.ui.plainTextEdit.clear()
        date = self.ui.calendarWidget.selectedDate()
        search_str = str(QString.toUtf8(self.ui.lineEdit.displayText()))
        text = init.search_csv(
                init.get_filelist(
                    str(date.month()), str(date.day()), str(date.year()), str(self.ui.comboBox.currentIndex())),
               search_str)

        files = init.get_filelist(
                    str(date.month()), str(date.day()), str(date.year()), str(self.ui.comboBox.currentIndex()))
        for row in text:
            self.ui.plainTextEdit.appendPlainText(row)

 #       self.ui.plainTextEdit.setPlainText(str(text))

#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('ReestrQt')

    # create widget
    w = MainWindow()
    w.setWindowTitle('ReestrQt')
    w.show()

    # connection
    QObject.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))

    # execute application
    sys.exit(app.exec_())