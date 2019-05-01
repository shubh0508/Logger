from multiprocessing import Queue
import random
# from multiprocessing.Manager import Queue

class BaseSharedQueue:

	# static dictionary of shared queues
	# key : name of queue
	# value : list of queues
	__qDict = dict()

	# const
	CONST_MAX_QUEUES_ALLOWED = 5
	CONST_MAX_QUEUE_SIZE_ALLOWED = 100
	CONST_QUEUE_TYPE_LOCAL = 'local_multiprocessing_queue';

	def __init__ (self, queueName, numberOfQueues = 1, queueType = CONST_QUEUE_TYPE_LOCAL):

		self.queueName = queueName
		self.currentNumberOfQueues = 0

		#for extending to multiple queues
		self.numberOfQueues = 1

		#for extending the queues to use Redis or MemCache
		self.queueType = queueType

		self.__initalizeQueues()

	def getQueueName(self):
		return self.queueName


	def __initalizeQueues(self):
		if self.queueName not in self.__qDict:
			self.__qDict[self.queueName] = []
			self.addQueues(self.numberOfQueues)

	## will return the queue based on the queue type
	def __getNewQueueInstance(self):
		if self.queueType == self.CONST_QUEUE_TYPE_LOCAL :
			return Queue(maxsize=self.CONST_MAX_QUEUE_SIZE_ALLOWED)



	## adds the empty
	def addQueues(self, numberOfQueues : int):
		if numberOfQueues < 1:
			raise Exception('Invalid number of queues : {numberOfQueues}')

		if numberOfQueues > self.CONST_MAX_QUEUES_ALLOWED - self.currentNumberOfQueues:
			raise Exception("""Adding {numberOfQueues} queues will be cross \\
				the maximum number of queues allowed""")

		for i in range(numberOfQueues):
			self.__qDict[self.queueName].append(self.__getNewQueueInstance())
		self.currentNumberOfQueues += numberOfQueues

		return

	#return the number of queues present with the given queueName
	def getCurrentNumberOfQueues(self):
		return self.currentNumberOfQueues


	## queue number starts from 0 to currentNumberOfQueues -1
	## if queue number is not present in the above range
	## then a random queue will be given
	def getQueue(self, queueNumber = -1):

		if queueNumber == -1:
			queueNumber = random.randint(0,self.currentNumberOfQueues)
		else:
			queueNumber = queueNumber % self.currentNumberOfQueues

		queueList = self.__qDict[self.queueName]

		return queueList[queueNumber]
