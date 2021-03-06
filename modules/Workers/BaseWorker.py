import atexit
import sys
from multiprocessing import Queue, Process
from modules.Logger.LogData import LogData
from modules.Sink.AbstractSink import AbstractSink
from modules.Queues.SharedBaseQueue import SharedBaseQueue

class BaseWorker(Process):

	"""Parent class for other workers. The other workers
	need to set the queue and execute consume operation.
	The consumer does blocking pop operations from the queue.
	Each worker process listens to only one of the  queues.
	Also the shutdown hooks are implemented to inform the
	Start and stop of the worker and any other errors.

	Also currently only multiprocessing.manager.queues are used
	directly, but a wrapper needs be implemented for it.
	And this worker should only take the queue of the that wrapper.
	Thus leaving the specific detail of the queues
	"""

	def __init__(self, taskQueueName : str, sink : AbstractSink, workerName : str):
		Process.__init__(self)
		self.__sink = sink
		self.__workerName = workerName

		## Queue Manager needs to be implemented for this
		self.__SBQ = SharedBaseQueue(taskQueueName)
		self.__taskQueue = self.__getQueue()

	def __getQueue(self, queueNumber = -1):
		if queueNumber == -1:
			return self.__SBQ.getQueue()
		return self.__SBQ.getQueue(queueNumber)

	def getTaskQueue(self):
		return self.__taskQueue

	## block pop from the task queue
	def getTask(self):
		return self.getTaskQueue().get()

	## returns the name of the spawned worker
	def getWorkerName(self):
		return self.__workerName

	## worker specific function
	def processTask(self, nextTask):
		print("task processed at worker : ", self.getWorkerName(), nextTask.getAllData())
		self.__sink.logData(nextTask)
        #raise NotImplementedError("processTask not implemented for the worker")


    ## adding hooks for getting the reason of worker stopped
	@atexit.register
	def addShutDownHook():
		print(" Worker Exited successfully!!! ")


	def run(self):
		print(self.getWorkerName(), " Worker started running successfully!!!")

		while True:
			nextTask = self.getTask()
			if nextTask is None:
				# Poison pill
				print(self.getWorkerName(), " Worker stopped successfully from poison pill!!!")
				self.addShutDownHook()
				break

			self.processTask(nextTask)

		return
