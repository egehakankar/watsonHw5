# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyQt5 import QtWidgets
import window
import sys


class ContentWrapper:
    def __init__(self, content):
        self.content = content
    def getContent(self):
        return self.content
    def setContent(self, content):
        self.content= content

def setWindowOneContent(text):
    global c1
    c1.setContent(text)


def setWindowTwoContent(text):
    global c2
    c2.setContent(text)


def showWindows():
    

    global c1
    global c2

    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    MainWindow2 = QtWidgets.QMainWindow()
    ui = window.Ui_MainWindow()
    ui2 = window.Ui_MainWindow()
    c1 = ContentWrapper("Hello")
    c2 = ContentWrapper("Hello2")
    ui.setupUi(MainWindow1, "Rules", c1)
    ui2.setupUi(MainWindow2, "Working Mind", c2, ui.refresh)
    MainWindow1.show()
    MainWindow2.show()
    print("Displaying application UI.")
    # c1.setContent("Test")
    # c2.setContent("Test2")

    app.exec_()
    print("UI window closed. Program will now exit.")


# Press the green button in the gutter to run the script.
# app = QtWidgets.QApplication(sys.argv)
# MainWindow1 = QtWidgets.QMainWindow()
# MainWindow2 = QtWidgets.QMainWindow()
# ui = window.Ui_MainWindow()
# ui2 = window.Ui_MainWindow()
# c1 = ContentWrapper("Hello")
# c2 = ContentWrapper("Hello2")
# ui.setupUi(MainWindow1, "Rules", c1)
# ui2.setupUi(MainWindow2, "Working Mind", c2, ui.refresh)
# MainWindow1.show()
# MainWindow2.show()
# print("Displaying application UI.")


if __name__ == '__main__':
    showWindows()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
