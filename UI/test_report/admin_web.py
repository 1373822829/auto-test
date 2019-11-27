#!/usr/bin/env python
#coding=utf-8
# name = input("what is your name?\n")
# print("Hello,"+name)
# input("Press <enter>")

#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import PyQt4.QtGui as QtGui
from PyQt4 import QtCore


class ProgressBarExample(QtGui.QWidget):

    def __init__(self):
        super(ProgressBarExample, self).__init__()

        self.initUI()

    def initUI(self):

        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.button = QtGui.QPushButton('开始', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(40, 80)

        self.connect(self.button, QtCore.SIGNAL('clicked()'),
                     self.doAction)

        self.timer = QtCore.QBasicTimer()
        self.step = 0

        self.setWindowTitle('ProgressBar')
        self.setGeometry(300, 300, 250, 150)


    def timerEvent(self, event):

        if self.step >= 100:
            self.timer.stop()
            self.button.setText('Restart')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive():
           # timer.started的状态
            self.timer.stop()
            self.button.setText('Continue')
        else:
            if self.step >= 100:
                self.step = 0
                # 清零
            self.timer.start(100, self)
            # start之后触发timerEvent
            self.button.setText('Stop')


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = ProgressBarExample()
    ex.show()
    app.exec_()

