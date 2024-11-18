# coding:utf-8
import sys

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, MSFluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont)
from qfluentwidgets import FluentIcon as FIF

from app.views.home_interface import HomeInterface
from app.views.demo import Widget
from app.views.setting_interface import SettingInterface


class MainWindow(MSFluentWindow):
    def __init__(self):
        super().__init__()

        self.homeInterface = Widget('Home Interface', self)
        self.toolInterface = Widget('Tool Interface', self)
        self.settingInterface = SettingInterface(self)

        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, "主页", FIF.HOME)
        self.addSubInterface(self.toolInterface, FIF.ROBOT, "工具箱", FIF.ROBOT)

        self.addSubInterface(self.settingInterface, FIF.SETTING, self.tr('设置'), FIF.SETTING,
                             NavigationItemPosition.BOTTOM)

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon('app/resource/images/logo.png'))
        self.setWindowTitle('工具箱')
