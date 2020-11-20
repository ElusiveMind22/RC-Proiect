import threading
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

"""
    This class creates the UI
"""


class UIManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.win = QMainWindow()

        # the 3 radio buttons Discover, Request, Decline
        self.rbutton1 = QtWidgets.QRadioButton(self.win)
        self.rbutton2 = QtWidgets.QRadioButton(self.win)
        self.rbutton3 = QtWidgets.QRadioButton(self.win)

        # Options you can set
        self.discoverOptions = [QtWidgets.QCheckBox("IP Address", self.win),
                                QtWidgets.QCheckBox("Parameter List", self.win)]
        self.requestOptions = [QtWidgets.QCheckBox("IP Addr.", self.win),
                               QtWidgets.QCheckBox("DHCP Server", self.win)]
        self.declineOptions = [QtWidgets.QCheckBox("Declined IP Address", self.win), ]

        # send button
        self.sendButton = QtWidgets.QPushButton("Send", self.win)

        # text box for input
        self.textBoxIP = QtWidgets.QLineEdit(self.win)

        # text edit, used to display text, so it's only for output
        self.display=QtWidgets.QTextEdit(self.win)

        self.__Config()

    def __Config(self):
        self.win.setGeometry(0, 0, 1200, 600)
        self.win.setWindowTitle("DHCP Client")

        label1 = QtWidgets.QLabel(self.win)
        label1.setText("Message type:")
        label1.move(10, 10)

        label2 = QtWidgets.QLabel(self.win)
        label2.setText("DCHP Options:")
        label2.setGeometry(200, 10, 100, 30)

        self.rbutton1.setGeometry(10, 50, 70, 30)
        self.rbutton1.setObjectName("Discover")
        self.rbutton1.setText("Discover")
        self.rbutton1.toggled.connect(self.__onDiscover)
        self.rbutton1.setChecked(True)

        self.rbutton2.setGeometry(10, 90, 70, 30)
        self.rbutton2.setObjectName("Request")
        self.rbutton2.setText("Request")
        self.rbutton2.toggled.connect(self.__onRequest)

        self.rbutton3.setGeometry(10, 130, 70, 30)
        self.rbutton3.setObjectName("Decline")
        self.rbutton3.setText("Decline")
        self.rbutton3.toggled.connect(self.__onDecline)

        self.sendButton.setGeometry(1120, 550, 70, 40)
        self.sendButton.clicked.connect(self.__onSend)

        self.display.setGeometry(750, 10, 440, 540)

        self.display.setReadOnly(True)

        # set the positions for options
        xpos = 200
        ypos = 50
        yscale = 40
        width = 150
        heigth = 30
        for i in range(0, len(self.discoverOptions)):
            self.discoverOptions[i].setGeometry(xpos, ypos + i * yscale, width, heigth)
        for i in range(0, len(self.requestOptions)):
            self.requestOptions[i].setGeometry(xpos, ypos + i * yscale, width, heigth)
            self.requestOptions[i].setHidden(True)
        for i in range(0, len(self.declineOptions)):
            self.declineOptions[i].setGeometry(xpos, ypos + i * yscale, width, heigth)
            self.declineOptions[i].setHidden(True)

        # text boxes should be configured here
        self.textBoxIP.setGeometry(xpos+width, ypos, width, heigth)
        self.textBoxIP.setHidden(True)

    def __onDiscover(self):
        if self.rbutton1.isChecked():
            print("Discover was clicked")
            for i in range(0, len(self.discoverOptions)):
                self.discoverOptions[i].setHidden(False)
        else:
            for i in range(0, len(self.discoverOptions)):
                self.discoverOptions[i].setHidden(True)
                self.discoverOptions[i].setChecked(False)

    def __onRequest(self):
        if self.rbutton2.isChecked():
            print("Request was clicked")
            for i in range(0, len(self.requestOptions)):
                self.requestOptions[i].setHidden(False)
            self.textBoxIP.setHidden(False)
        else:
            for i in range(0, len(self.requestOptions)):
                self.requestOptions[i].setHidden(True)
                self.requestOptions[i].setChecked(False)
            self.textBoxIP.setHidden(True)
            self.textBoxIP.setText("")

    def __onDecline(self):
        if self.rbutton3.isChecked():
            print("Decline was clicked")
            for i in range(0, len(self.declineOptions)):
                self.declineOptions[i].setHidden(False)
            self.textBoxIP.setHidden(False)
        else:
            for i in range(0, len(self.declineOptions)):
                self.declineOptions[i].setHidden(True)
                self.declineOptions[i].setChecked(False)
            self.textBoxIP.setHidden(True)
            self.textBoxIP.setText("")
    def __onSend(self):
        print("Package sent!")
        # TO_DO
        # when you press the send button:
        #   you must consider the case where you send
        # a packet and wait for the reply but the user wants
        # to send another packet
        #   you must read the options selected
        # and send those options to a Packet manager
        #   as soon as you send something you should
        # disable the send button from being used,
        # only the Packet manager can enable the button again

    def startUI(self):
        self.win.show()
        sys.exit(self.app.exec_())
