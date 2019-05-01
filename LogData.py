# class for Log Data object
# contains timestamp, level, messageNamespace, messageContent

from Levels import Levels
from datetime import datetime


class LogData():

	def __init__ (self, level : Levels, messageNamespace : str, messageContent = dict()):
		self._level = level
		self._messageNamespace = messageNamespace
		self._messageContent  = messageContent
		self._logTime = datetime.today()

	def getLevel(self):
		return self._level

	def getMessageNamespace(self):
		return self._messageNamespace

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
		data['level'] = self._level.value
		data['messageNamespace'] = self._messageNamespace
		data['messageContent'] = self._messageContent
		data['logTime'] = self.getLogTime('str')

		return data

