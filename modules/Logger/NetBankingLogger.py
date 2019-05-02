from modules.Logger.Logger import Logger

class NetBankingLogger(Logger):
	"""docstring for UPILogger"""

	SETTINGS_KEY = 'netBankingLogger'

	def __init__(self, arg = []):

		self.__configuration = self.getConfigurationFromSettings()
		super(NetBankingLogger, self).__init__(self.__configuration)


	def getConfigurationFromSettings(self):

		###getting configurations from settings (to be implemented)
		#configuration = settings.getSetting(SETTINGS_KEY)

		configuration = {'queueName' : 'netBankingLogs'}
		return configuration