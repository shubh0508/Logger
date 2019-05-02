from modules.Enum.Levels import Levels
from datetime import datetime


class LogData():
	# class for Data Type of Log objects
	# contains timestamp, level, messageName, messageContent


	def __init__(self,
		level : Levels,
		messageName : str,
		messageContent = dict(),
		tsFormat = 'str'):

		self.__level = level
		self.__messageName = messageName
		self.__messageContent  = messageContent
		self.__logTime = datetime.today()
		self.__tsFormat = tsFormat

	def getLevel(self):
		return self.__level.value

	def getMessageName(self):
		return self.__messageName

	def getMessageContent(self):
		return self.__messageContent

	# two formats supported i.e. str or timestamp
	# timestamp will be returned if format is any other than str
	def getLogTime(self):

		return self.__logTime.strftime(self.__tsFormat)

	def getAllData(self):

		data = {}
		data['level'] = self.getLevel()
		data['messageName'] = self.getMessageName()
		data['messageContent'] = self.getMessageContent()
		data['logTime'] = self.getLogTime()

		return data

