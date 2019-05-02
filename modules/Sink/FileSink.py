import os
import time
from datetime import datetime
from modules.Sink.AbstractSink import AbstractSink
from modules.Logger.LogData import LogData


class FileSink(AbstractSink):
	"""Implementing file type sink"""

	CONST_DEFULT_LOG_FILE = 'tmp/logger.log'

	def __init__(self, configuration):
		super(FileSink, self).__init__(configuration)
		self.__configuration = configuration

		if self.__checkConfiguration() == False :
			raise Exception('Incorrect configuration provided ' + str(configuration))

		## name of the log file, not required currently
		# self.__fileName = configuration['filename']

		## path of the log file
		## assumption file extension is log
		self.__filePath = configuration['filePath']

		## if false then the earlier file will be version with timestamp
		self.__appendFlag = configuration['append'] if 'append' in configuration else True

		self.__fileObject = None
		self.__getFileObject()
		self.__versionOldFile()

	def __versionOldFile(self):

		if self.__appendFlag == False and os.path.isfile(self.__filePath) == True :

			## removing .log from path
			versionedFilepath = self.__filePath[:-5]
			versionedFilepath += '_versioned_at_' + str(time.time())
			versionedFilepath += datetime.today().strftime('%Y_%m_%d_%H_%M_%S') + '.log'
			print('versionedFilepath : ', versionedFilepath)
			os.rename(self.getFilePath(), versionedFilepath)

	def __getFileObject(self):
		if self.__fileObject is None or os.path.isfile(self.__filePath) == False:
			self.__fileObject = open(self.__filePath, 'a')

		return self.__fileObject

	def getFilePath(self):

		path = 'tmp.log'
		if self.__filePath is not None:
			path = self.__filePath

		return path

	def __checkConfiguration(self):
		return True

	def close(self):
		if self.__fileObject is not None:
			self.__fileObject.close()

	def logData(self, data : LogData):

		dataDict = data.getAllData()
		dataDict['logged_at'] = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')

		# only write and flush so not an extra funtion is created
		self.__getFileObject().write(str(dataDict) + '\n')
		self.__getFileObject().flush()

		return

	def catLogFile(self):

		if os.path.isfile(self.getFilePath()):
			bashCommand = 'cat ' + self.getFilePath()
			os.system(bashCommand)
		else :
			raise Exception('File Not found exception ' + str(self.getFilePath()))
