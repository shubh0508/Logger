from modules.Logger.LogData import LogData
from modules.Sink.DatabaseSink import DatabaseSink
from modules.Enum.Levels import Levels

ldata = LogData(Levels.INFO, 'abc', ['efg', 'ijk'])
print('ldata', ldata.getAllData())


DB_CONFIGS = {}
DB_CONFIGS['host'] = '127.0.0.1'
DB_CONFIGS['username'] = 'shubh'
DB_CONFIGS['password'] = ''
DB_CONFIGS['database'] = 'logdb'

DB_SINK_CONFIGURATIONS = {'database_configurations' : DB_CONFIGS}

sink = DatabaseSink(DB_SINK_CONFIGURATIONS)
sink.logData(ldata)
sink.logData(ldata)
sink.logData(ldata)
