from LogData import LogData
from Levels import Levels
from DatabaseSink import DatabaseSink

		# data = {}
		# data['level'] = 'info'
		# data['messageNamespace'] = 'abc'
		# data['messageContent'] = 'efg'
		# data['logTime'] = '2019-01-31 00:00:00'


ldata = LogData(Levels.INFO, 'abc', 'efg')
print('ldata', ldata)


DB_CONFIGS = {}
DB_CONFIGS['host'] = '127.0.0.1'
DB_CONFIGS['username'] = 'shubh'
DB_CONFIGS['password'] = ''
DB_CONFIGS['database'] = 'logdb'

DB_SINK_CONFIGURATIONS = {'database_configurations' : DB_CONFIGS}

sink = DatabaseSink(DB_SINK_CONFIGURATIONS)
sink.logData(ldata)


# database = 'logdb', user = "shubh", password = "", host = "127.0.0.1", port ="5432"
# connection = psycopg2.connect(database = 'logdb', user = "shubh", password = "", host = "127.0.0.1", port ="5432")

# "INSERT INTO logtable (level, mmessage_namespace, message_content, log_time)
# VALUES ('info', 'abc', 'efg', '2019-05-01 09:07:50');"