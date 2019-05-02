from multiprocessing import Queue
import random
# from multiprocessing.Manager import Queue

class SharedBaseQueue:

	# static dictionary of shared queues
	# key : name of queue
	# value : list of queues
	__qDict = dict()

	# const
	CONST_MAX_QUEUES_ALLOWED = 5
	CONST_MAX_QUEUE_SIZE_ALLOWED = 100
	CONST_QUEUE_TYPE_LOCAL = 'local_multiprocessing_queue';
	currentNumberOfQueues = 0

	def __init__ (self, queueName, numberOfQueues = 1, queueType = CONST_QUEUE_TYPE_LOCAL):

		self.queueName = queueName

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

		if self.numberOfQueues > self.currentNumberOfQueues:
			self.addQueues(self.numberOfQueues - self.currentNumberOfQueues)

	## will return the queue based on the queue type
	def __getNewQueueInstance(self):
		if self.queueType == self.CONST_QUEUE_TYPE_LOCAL :
			return Queue(maxsize=self.CONST_MAX_QUEUE_SIZE_ALLOWED)


	## adds the empty
	def addQueues(self, numberOfQueues : int):
		if numberOfQueues < 1:
			raise Exception('Invalid number of queues : {numberOfQueues}')

		if numberOfQueues > self.CONST_MAX_QUEUES_ALLOWED - self.currentNumberOfQueues:
			raise Exception("Adding queues will cross the maximum number of queues allowed")

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

		queueNumber = 0
		if queueNumber == -1:
			queueNumber = random.randrange(0, self.currentNumberOfQueues)

		elif self.currentNumberOfQueues > 0:
			queueNumber = queueNumber % self.currentNumberOfQueues

		print('queueNumber at getQueue ', queueNumber)
		queueList = self.__qDict[self.queueName]

		return queueList[queueNumber]
