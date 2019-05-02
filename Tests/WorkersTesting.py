from modules.Logger.LogData import LogData
from modules.Enum.Levels import Levels
from modules.Sink.FileSink import FileSink
from modules.Queues.SharedBaseQueue import SharedBaseQueue
from modules.Workers.BaseWorker import BaseWorker
from modules.Logger.NetBankingLogger import NetBankingLogger

ldata = LogData(Levels.INFO, 'abc', 'efg')
print('ldata', ldata)

nLogger = NetBankingLogger()

nLogger.info('mesg1', ['adffffa','fads'])
nLogger.info('mesg2', ['adffffa','fads'])
nLogger.info('mesg3', ['adffffa','fads'])

q = nLogger._Logger__getQueue()
print(q.get().getAllData())



DB_SINK_CONFIGURATIONS = {'append' : True, 'filePath' : 'logger.logs'}
sink = FileSink(DB_SINK_CONFIGURATIONS)

#net banking queue configuration
configuration = {'queueName' : 'netBankingLogs'}
SBQ = SharedBaseQueue(configuration['queueName'])
print("number of queues: ", SBQ.getCurrentNumberOfQueues())
task_queue = SBQ.getQueue()
worker_name = 'NetBankingWorker'




netBankingWorker =  BaseWorker(task_queue, sink, worker_name)