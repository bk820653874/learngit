from PyQt5 import QtGui, QtWidgets
from gui_01 import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def weather_search(self):
        from api import request1
        res = request1("POST", self.textEdit.toPlainText())
        # print(type(res['forecast'][0]['date']))
        self.textBrowser.insertPlainText("     %s\n" % res['forecast'][0]['date'])
        self.textBrowser.insertPlainText("      %s ～ %s\n" % (res['forecast'][0]['low'][-3:-1],\
                                                           res['forecast'][0]['high'][-3:-1]))
        self.textBrowser.insertPlainText("        %s\n" % res['forecast'][0]['type'])
        self.textBrowser.insertPlainText("      风力：%s\n" % res['forecast'][0]['fengli'][-5:-3])
        self.textBrowser.insertPlainText("     %s\n" % res['forecast'][0]['fengxiang'])
        self.textBrowser.insertPlainText("今日建议：%s\n" % res['ganmao'])



def main():
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.pushButton.clicked.connect(ui.weather_search)
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
