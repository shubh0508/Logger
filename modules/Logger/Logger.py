from modules.Logger.LogData import LogData
from modules.Enum.Levels import Levels
from modules.Queues.SharedBaseQueue import SharedBaseQueue
from modules.Logger.LevelLogger import LevelLogger


class Logger():
	"""
	Queue for logger is fetch from configuration while constructing the logger
	The logs are the then push using
	"""
	def __init__(self, configuration):

		self.__configuration = configuration
		self.__checkConfiguration()

		#dictionary for level logger objects
		self.__levelLogger = {}


	def __checkConfiguration(self):

		# assert('queueName' in self.__configuration), 'queue name not found in configuration'
		# assert('workerName' in self.__configuration), 'worker name not found in configuration'
		## and many more assertion to be included

		return True

	def getConfigurationForLevel(self, level : Levels):

		assert(level.value in self.__configuration), """settings for level: {level}
		not found for the current stream""".format(level = level.value)

		return self.__configuration[level.value]

	def getLoggerFromLevel(self, level : Levels):

		# print(level.value, self.getConfigurationForLevel(level))

		if level.value not in self.__levelLogger:
			levelLogger = LevelLogger(level.INFO, self.getConfigurationForLevel(level))
			self.__levelLogger[level.value] = levelLogger

		return self.__levelLogger[level.value]

	def info(self, messageNamespace, messageContent):

		levelLogger = self.getLoggerFromLevel(Levels.INFO)
		levelLogger.log(messageNamespace, messageContent)
		print(messageNamespace, messageContent)

	def debug(self, messageNamespace, messageContent):

		levelLogger = self.getLoggerFromLevel(Levels.DEBUG)
		levelLogger.log(messageNamespace, messageContent)

	def warn(self, messageNamespace, messageContent):

		levelLogger = self.getLoggerFromLevel(Levels.WARN)
		levelLogger.log(messageNamespace, messageContent)

	def error(self, messageNamespace, messageContent):

		levelLogger = self.getLoggerFromLevel(Levels.ERROR)
		levelLogger.log(messageNamespace, messageContent)

	def fatal(self, messageNamespace, messageContent):

		levelLogger = self.getLoggerFromLevel(Levels.FATAL)
		levelLogger.log(messageNamespace, messageContent)

