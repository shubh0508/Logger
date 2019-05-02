import json
from modules.Sink.AbstractSink import AbstractSink
from modules.Sink.Database import Database
from modules.Logger.LogData import LogData

class DatabaseSink(AbstractSink):
	"""docstring for DatabaseSink"""

	def __init__(self, configuration):
		# super(DatabaseSink, self).__init__(configuration)
		self.__configuration = configuration
		if self.__checkConfiguration() == False:
			raise Exception('Incorrect configuration provided ' + str(configuration))

		self.__DB = Database(configuration['database_configurations'])

	def __checkConfiguration(self):
		return True

	def logData(self, data : LogData):
		dataDict = data.getAllData();

		sql = """INSERT INTO log_table (level, mmessage_namespace, message_content, log_time) \
			VALUES ('{level}', '{message_namespace}', '{message_content}', '{log_time}')""". \
			format(level = dataDict['level'], message_namespace = dataDict['messageName'],
				message_content = json.dumps(dataDict['messageContent']), log_time = dataDict['logTime'])

		# print('sql', sql)
		self.__DB.executeQuery(sql)

		return