from modules.Logger.LogData import LogData
from modules.Enum.Levels import Levels
from modules.Queues.SharedBaseQueue import SharedBaseQueue


class LevelLogger():
	"""
	Queue for logger is fetch from configuration while constructing the logger
	The logs are the then push using
	"""
	def __init__(self, level, configuration):

		self.__configuration = configuration
		self.__checkConfiguration()

		self.queueName = configuration['queueName']
		self.tsFormat = configuration['tsFormat']
		self.level = level

		self.numberOfQueues = 1
		if configuration['threadModel'] == 'MULTI':
			numberOfQueues = configuration['numberOfQueues']

		self.__SBQ = SharedBaseQueue(self.queueName, self.numberOfQueues)
		self.__logQueue = self.__getQueue()

	def __checkConfiguration(self):
		# print('__checkConfiguration', configuration)
		assert('queueName' in self.__configuration), 'queue name not found in configuration'
		assert('workerName' in self.__configuration), 'worker name not found in configuration'
		## and many more assertion to be included

	def __getQueue(self, queueNumber = 0):
		return self.__SBQ.getQueue(queueNumber)

	def pushLog(self, logData):
		self.__logQueue.put(logData)

	def log(self, messageNamespace, messageContent):

		## currently its a blocking put
		## but it should be put_no_wait with a timeout
		## based on settings depending on the importance of logs
		logData = LogData(self.level, messageNamespace, messageContent, self.tsFormat)
		self.pushLog(logData)
