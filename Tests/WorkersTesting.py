from modules.Logger.LogData import LogData
from modules.Enum.Levels import Levels
from modules.Sink.FileSink import FileSink
from modules.Queues.SharedBaseQueue import SharedBaseQueue
from modules.Workers.BaseWorker import BaseWorker
from modules.Logger.NetBankingLogger import NetBankingLogger
from modules.Workers.NetBankingLogINFOWorker import NetBankingLogINFOWorker

ldata = LogData(Levels.INFO, 'abc', 'efg')
print('ldata', ldata)

nLogger = NetBankingLogger()

nLogger.info('mesg11', ['adffffa','fads'])
nLogger.info('mesg21', ['adffffa','fads'])
nLogger.info('mesg31', ['adffffa','fads'])


DB_SINK_CONFIGURATIONS = {'append' : True, 'filePath' : 'logger.logs'}
sink = FileSink(DB_SINK_CONFIGURATIONS)

#net banking queue configuration
configuration = {'queueName' : 'netBankingLogInfoQueue'}
SBQ = SharedBaseQueue(configuration['queueName'])
print("number of queues: ", SBQ.getCurrentNumberOfQueues())
task_queue = SBQ.getQueue()
worker_name = 'NetBankingWorker'

netBankingWorker =  NetBankingLogINFOWorker()
netBankingWorker.start()


#the worker picks these up itself
nLogger.info('mesg11', ['adffffa','fads'])
nLogger.info('mesg13', ['adffffa','fads'])
nLogger.info('mesg14', ['adffffa','fads'])


#thus the worker is running as expected
