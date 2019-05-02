from modules.Logger.LogData import LogData
from modules.Enum.Levels import Levels
from modules.Sink.FileSink import FileSink

ldata = LogData(Levels.INFO, 'abc', 'efg')
print('ldata', ldata)

DB_SINK_CONFIGURATIONS = {'append' : True, 'filePath' : 'logger.logs'}


sink = FileSink(DB_SINK_CONFIGURATIONS)
sink.logData(ldata)
sink.logData(ldata)
sink.logData(ldata)

sink.catLogFile()

sink.logData(ldata)
sink.logData(ldata)
sink.logData(ldata)

sink.catLogFile()


###############################################

DB_SINK_CONFIGURATIONS = {'append' : True, 'filePath' : 'logger.logs'}
sink1 = FileSink(DB_SINK_CONFIGURATIONS)
sink1.logData(ldata)
sink1.logData(ldata)
sink1.logData(ldata)

sink1.catLogFile()


## Versioning of the previous file
DB_SINK_CONFIGURATIONS = {'append' : False, 'filePath' : 'logger.logs'}
sink2 = FileSink(DB_SINK_CONFIGURATIONS)
sink2.logData(ldata)
sink2.logData(ldata)
sink2.logData(ldata)
sink2.catLogFile()

sink.catLogFile()
sink1.catLogFile()
sink2.catLogFile()
