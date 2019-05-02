from modules.Enum.Levels import Levels
from datetime import datetime


class LogData():
	# class for Data Type of Log objects
	# contains timestamp, level, messageName, messageContent


	def __init__ (self, level : Levels, messageName : str, messageContent = dict()):
		self._level = level
		self._messageName = messageName
		self._messageContent  = messageContent
		self._logTime = datetime.today()

	def getLevel(self):
		return self._level

	def getMessageName(self):
		return self._messageName

	def getMessageContent(self):
		return self._messageContent

	# two formats supported i.e. str or timestamp
	# timestamp will be returned if format is any other than str
	def getLogTime(self, format = 'str'):

		if format == 'str':
			return self._logTime.strftime('%Y-%m-%d %H:%M:%S')
		else :
			return self._logTime

	def getAllData(self):

		data = {}
		data['level'] = self.getLevel().value
		data['messageName'] = self.getMessageName()
		data['messageContent'] = self.getMessageContent()
		data['logTime'] = self.getLogTime('str')

		return data

