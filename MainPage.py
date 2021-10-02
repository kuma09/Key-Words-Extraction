# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:39:48 2019

@author: Force Technologies
"""
import s
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MainPage(QDialog):
	def __init__(self):
		super(MainPage,self).__init__()
		loadUi('first-ui.ui',self)
		self.pushButton.clicked.connect(self.move)

	def move(self):	
		from SecPage import SecPage
		theclass=SecPage()
		theclass.exec_()

	



app= QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())