from modules.Logger.LogData import LogData
from modules.Enum.Levels import Levels
from modules.Sink.FileSink import FileSink
from modules.Sink.DatabaseSink import DatabaseSink
from modules.Queues.SharedBaseQueue import SharedBaseQueue
from modules.Workers.BaseWorker import BaseWorker
from modules.Logger.NetBankingLogger import NetBankingLogger

ldata = LogData(Levels.INFO, 'abc', 'efg')
# print('ldata', ldata.getAllData())

DB_CONFIGS = {}
DB_CONFIGS['host'] = '127.0.0.1'
DB_CONFIGS['username'] = 'shubh'
DB_CONFIGS['password'] = ''
DB_CONFIGS['database'] = 'logdb'
DB_SINK_CONFIGURATIONS = {'database_configurations' : DB_CONFIGS}

qConfiguration = {'queueName' : 'netBankingLogs'}


nLogger = NetBankingLogger()
# nLogger.info('mesg1', ['adffffa','fads'])
# nLogger.info('mesg2', ['adffffa','fads'])
# nLogger.info('mesg3', ['adffffa','fads'])

#net banking queue configuration
sink = DatabaseSink(DB_SINK_CONFIGURATIONS)
SBQ = SharedBaseQueue(qConfiguration['queueName'])
print("number of queues: ", SBQ.getCurrentNumberOfQueues())
taskQueue = SBQ.getQueue()
workerName = 'NetBankingWorker'

# ADDING 5 worker processes

workerList = []
for i in range(10):
	#net banking queue configuration
	sink = DatabaseSink(DB_SINK_CONFIGURATIONS)

	SBQ = SharedBaseQueue(qConfiguration['queueName'])
	# print("number of queues: ", SBQ.getCurrentNumberOfQueues())

	taskQueue = SBQ.getQueue()
	currentWorkerName = workerName + "_v" + str(i)

	workerList.append(BaseWorker(taskQueue, sink, currentWorkerName))

for worker in workerList:
	worker.start()

for i in range(10):
	nLogger.info('mesgs_v' + str(i), ['adffffa','fads'])
	nLogger.error('mesgs_v' + str(i), ['adffffa','fads'])
	nLogger.fatal('mesgs_v' + str(i), ['adffffa','fads'])

