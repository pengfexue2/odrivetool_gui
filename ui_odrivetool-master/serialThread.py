

from PyQt5 import QtCore, QtGui, QtWidgets
import odrive
import time
from fibre.utils import Logger


class ODriveWorker(QtCore.QThread):
	# add some signals here
	odrive_found_sig = QtCore.pyqtSignal('PyQt_PyObject')
	def __init__(self, my_drive):
		QtCore.QThread.__init__(self)
		self._isRunning = True
		self.my_drive = my_drive


	def stop(self):
		self._isRunning = False

	def run(self):
		self.odrive_found_sig.emit(self.my_drive)

