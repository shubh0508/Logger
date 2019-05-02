from modules.Logger.Logger import Logger
from modules.setting import Settings

class NetBankingLogger(Logger):
	"""docstring for UPILogger"""

	SETTINGS_KEY = 'netBankingLogger'

	def __init__(self, arg = []):

		self.__configuration = self.getConfigurationFromSettings()
		self.__checkConfiguration()
		# print('__configuration', self.__configuration)

		super(NetBankingLogger, self).__init__(self.__configuration)

	def __checkConfiguration(self):

		# assert('queueName' in self.__configuration), 'queue name not found in configuration'
		# assert('workerName' in self.__configuration), 'worker name not found in configuration'
		## and many more assertion to be included

		return True

	def getConfigurationFromSettings(self):

		###getting configurations from settings (to be implemented)
		settings = Settings()
		configuration = settings.get(self.SETTINGS_KEY)
		assert(len(configuration) > 0), 'configurations not found in \
		settings for key: ' + self.SETTINGS_KEY

		return configuration
