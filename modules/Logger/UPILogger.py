from Logger import Logger

class UPILogger(Logger):
	"""docstring for UPILogger"""

	SETTINGS_KEY = 'upiLogger'

	def __init__(self, arg):

		self.__configuration = self.getConfigurationFromSettings()
		super(UPILogger, self).__init__(self.__configuration)


	def getConfigurationFromSettings(self):

		###getting configurations from settings (to be implemented)
		#configuration = settings.getSetting(SETTINGS_KEY)

		configuration = {'queueName' : 'upiLogs'}
		return configuration