from Sink import Sink
from Database import Database
from LogData import LogData

class DatabaseSink(Sink):
	"""docstring for DatabaseSink"""
	def __init__(self, configuration):
		super(DatabaseSink, self).__init__(configuration)
		self.__configuration = configuration
		if self.__checkConfiguration() == False:
			raise Exception('Incorrect configuration provided ' + str(configuration))

		self.__DB = Database(configuration['database_configurations'])

	def __checkConfiguration(self):
		return True

	def logData(self, data : LogData):
		dataDict = data.getAllData();
		# data = {}
		# data['level'] = self._level
		# data['messageNamespace'] = self._messageNamespace
		# data['messageContent'] = self._messageContent
		# data['logTime'] = self.getLogTime('str')

		sql = "INSERT INTO log_table (level, mmessage_namespace, message_content, log_time) \
			VALUES ('{level}', '{mmessage_namespace}', '{message_content}', '{log_time}')".format(
				level = dataDict['level'], mmessage_namespace = dataDict['messageNamespace'],
				message_content = dataDict['messageContent'], log_time = dataDict['logTime'])


		print('sql', sql)
		self.__DB.executeQuery(sql)

		return