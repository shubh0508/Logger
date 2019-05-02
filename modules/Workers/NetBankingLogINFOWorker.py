from modules.Workers.BaseWorker import BaseWorker
from modules.Sink.DatabaseSink import DatabaseSink
from modules.Sink.FileSink import FileSink
from modules.setting import Settings
from modules.Enum.Levels import Levels

class NetBankingLogINFOWorker(BaseWorker):
	"""docstring for NetBankingWorker"""
	SETTINGS_KEY = 'netBankingLogger'

	def __init__(self, arg = []):

		self.__configuration = self.getConfigurationFromSettings()
		print('__configuration', self.__configuration)

		self.queueName = self.__configuration['queueName']
		self.workerName = self.__configuration['workerName']

		## here SinkManager should be implemented
		if self.__configuration['sinkType'] == 'DB':
			self.sink = DatabaseSink(self.__configuration['sinkConfig'])
		else:
			self.sink = FileSink(self.__configuration['sinkConfig'])

		super(NetBankingLogINFOWorker, self).__init__(self.queueName, self.sink, self.workerName)


	def getConfigurationFromSettings(self):

		###getting configurations from settings (to be implemented)
		settings = Settings()
		configuration = settings.get(self.SETTINGS_KEY)
		assert(len(configuration) > 0), 'configurations not found in \
		settings for key: ' + self.SETTINGS_KEY


		return configuration[Levels.INFO.value]