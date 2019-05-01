from Sink import Sink
import os
import datetime
import json
from LogData import LogData

class FileSink(Sink):
	"""docstring for FileSink"""
	def __init__(self, configuration):
		super(FileSink, self).__init__()
		self.__configuration = configuration

		if self.__checkConfiguration() == False :
			raise Exception('Incorrect configuration provided ' + str(configuration))

		## name of the log file, not required currently
		# self.__fileName = configuration['filename']

		## path of the log file
		## assumption file extension is log
		self.__filePath = configuration['__filePath']

		## if false then the earlier file will be version with timestamp
		self.__appendFlag = configuration['append']
		self.__fileObject = self.__getFileObject()

		self.__versionOldFile()
		self.__initFile()

	def __versionOldFile(self):

		if self.__appendFlag == False and os.path.isfile(self.__filePath) == True :

			## removing .log from path
			versionedFilepath = self.__filePath[:-4]
			versionedFilepath += '_versioned_at_'
			versionedFilepath += datetime.today().strftime('%Y_%m_%d_%H_%M_%S') + '.log'
			os.rename("path/to/current/file.foo", versionedFilepath)

	def __getFileObject(self):
		if self.__fileObject is None:
			self.__fileObject = open(self.__filePath, 'a')

		return self.__fileObject

	def __checkConfiguration(self):
		return True

	def close(self):
		if self.__fileObject is not None:
			self.__fileObject.close()

	def logData(data : LogData):

		dataDict = data.getAllData()
		dataDict['logged_at'] = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')

		# only write and flush so not an extra funtion is created
		self.__getFileObject().write(str(dataDict) + '\n')
		self.__getFileObject().flush()

		return

