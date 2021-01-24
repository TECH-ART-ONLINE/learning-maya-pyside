# coding: utf-8
from maya import cmds
from maya import OpenMayaUI as omui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance


def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(long(ptr), QWidget)
    return widget


class SimpleButtonUI(QWidget):    
    def __init__(self, *args, **kwargs):
        super(SimpleButtonUI, self).__init__(*args, **kwargs)

        # このウィジェットの親をMayaのメインウインドウに設定する。
        self.setParent(get_maya_main_window())

        # ウインドウのタイプを決める
        self.setWindowFlags(Qt.Window)

        # ウインドウのオブジェクト名とタイトル名を設定する
        self.setObjectName('simple_button')        
        self.setWindowTitle('Simple Button')

        # いろいろ作る部分
        # １．レイアウトを作る
        main_layout = QVBoxLayout(self)
        # ２．部品を作る
        buttonA = QPushButton("Button A", self)
        buttonB = QPushButton("Button B", self)
        # ３．部品をレイアウトに追加する
        main_layout.addWidget(buttonA)
        main_layout.addWidget(buttonB)
        # ４．部品をクリックした時の振る舞いを作る
        buttonA.clicked.connect(self.buttonA_onClicked)
        buttonB.clicked.connect(self.buttonB_onClicked)

    def buttonA_onClicked(self):
        cmds.polyCube()

    def buttonB_onClicked(self):
        cmds.polyCylinder()


window_instance = SimpleButtonUI()
window_instance.show()
