import atexit
from multiprocessing import Queue, Process
from modules.Logger.LogData import LogData
from modules.Sink.AbstractSink import AbstractSink

class BaseWorker(Process):
# class BaseWorker():


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

	def __init__(self, task_queue : Queue, sink : AbstractSink, workerName : str):
		Process.__init__(self)
		self.__task_queue = task_queue
		self.__sink = sink
		self.__workerName = workerName


	def getTaskQueue(self):
		return self.__task_queue

	## block pop from the task queue
	def getTask(self):
		return self.getTaskQueue().get()

	## returns the name of the spawned worker
	def getWorkerName(self):
		return self.__workerName

	## worker specific function
	def processTask(self, nextTask):
		print("task processed", nextTask.getAllData())
		self.__sink.logData(nextTask)
        #raise NotImplementedError("processTask not implemented for the worker")


    ## adding hooks for getting the reason of worker stopped
	@atexit.register
	def addShutDownHook(self):
		print(self.getWorkerName(), " Worker Exited successfully!!! ", sys.exc_info()[0])


	def run(self):
		print(self.getWorkerName(), " Worker started running successfully!!!")

		try:

			while True:
				nextTask = self.getTask()
				if nextTask is None:
					# Poison pill
					print(self.getWorkerName(), " Worker stopped successfully from poison pill!!!")
					self.addShutDownHook()
					break

				self.processTask(nextTask)

		except Exception as error:
			print("BaseWorker stopped due to error : ", error)
			self.addShutDownHook()

		return
