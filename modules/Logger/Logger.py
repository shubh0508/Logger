from modules.Logger.LogData import LogData
from modules.Enum.Levels import Levels
from modules.Queues.SharedBaseQueue import SharedBaseQueue


class Logger():
	"""
	Queue for logger is fetch from configuration while constructing the logger
	The logs are the then push using
	"""
	def __init__(self, configuration):

		self.__configuration = configuration
		if 'queueName' not in configuration:
			raise Exception('Incorrect configuration provided ' + str(configuration))

		queueName = configuration['queueName']
		self.__SBQ = SharedBaseQueue(queueName)
		self.__logQueue = self.__getQueue()

	def __getQueue(self, queueNumber = 0):
		return self.__SBQ.getQueue(queueNumber)

	def log(self, logData : LogData):

		## currently its a blocking put
		## but it should be put_no_wait with a timeout
		## based on settings depending on the importance of logs
		self.__logQueue.put(logData)

	def info(self, messageNamespace, messageContent):
		logLevel = Levels.INFO
		logData = LogData(logLevel, messageNamespace, messageContent)
		self.log(logData)

	def debug(self, messageNamespace, messageContent):
		logLevel = Levels.DEBUG
		logData = LogData(logLevel, messageNamespace, messageContent)
		self.log(logData)

	def warn(self, messageNamespace, messageContent):
		logLevel = Levels.WARN
		logData = LogData(logLevel, messageNamespace, messageContent)
		self.log(logData)

	def error(self, messageNamespace, messageContent):
		logLevel = Levels.ERROR
		logData = LogData(logLevel, messageNamespace, messageContent)
		self.log(logData)

	def fatal(self, messageNamespace, messageContent):
		logLevel = Levels.FATAL
		logData = LogData(logLevel, messageNamespace, messageContent)
		self.log(logData)

