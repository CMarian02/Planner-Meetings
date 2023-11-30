from PyQt6 import QtWidgets, QtCore, QtGui
from tools import * 


class UserPage(QtWidgets.QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle('Meetings Planner')
        self.resize(1000, 850)
        self.setMaximumSize(QtCore.QSize(1000, 850))
        self.setMinimumSize(QtCore.QSize(1000, 850))
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.profile_logo = QtWidgets.QLabel(self.centralwidget)
        self.profile_logo.setGeometry(100, 100, 200, 200)
        self.profile_logo.setObjectName('profile_logo')
        self.version_text = QtWidgets.QLabel('v0.0.1', self.centralwidget)
        self.version_text.setGeometry(965, 830, 70, 20)
        self.version_text.setObjectName('version_text')
        self.view_mett_button = QtWidgets.QPushButton('View Meetings', self.centralwidget)
        self.view_mett_button.setGeometry(10, 300, 100, 50)
        self.view_mett_button.setObjectName('view_mett_button')
        self.plan_meeting_button = QtWidgets.QPushButton('Plan Meeting', self.centralwidget)
        self.plan_meeting_button.setGeometry(10, 400, 100, 50)
        self.plan_meeting_button.setObjectName('plan_meeting_button')
        self.view_your_teams = QtWidgets.QPushButton('View Your Teams', self.centralwidget)
        self.view_your_teams.setGeometry(10, 500, 100, 50)  
        self.view_your_teams.setObjectName('view_teams_button')
        self.welcome_message = QtWidgets.QLabel(f'Welcome back in your account, {username}', self.centralwidget)
        self.welcome_message.setGeometry(325, 35, 350, 50)
        self.welcome_message.setObjectName('welcome_message')
        self.profile_icon = QtWidgets.QLabel(self.centralwidget)
        self.profile_icon.setGeometry(10, 15, 100, 100)
        self.profile_icon.setObjectName('profile_icon')
        self.profile_icon_text = QtWidgets.QLabel(f'{username[0].upper()}', self.centralwidget)
        self.profile_icon_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.profile_icon_text.setGeometry(10, 15, 100, 100)
        self.profile_icon_text.setObjectName('profile_icon_text')
        self.left_border = QtWidgets.QLabel(self.centralwidget)
        self.left_border.setGeometry(120, 0, 2, 850)
        self.left_border.setObjectName('left_border')
        self.top_border = QtWidgets.QLabel(self.centralwidget)
        self.top_border.setGeometry(120, 120, 880, 2)
        self.top_border.setObjectName('top_border')
        self.calendar_widget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar_widget.setGeometry(150, 150, 820, 670)
        self.calendar_widget.setObjectName('calendar_widget')
        