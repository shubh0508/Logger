import sys
from abc import ABC, abstractmethod
from modules.Logger.LogData import LogData

class AbstractSink(ABC):
	"""This class works as an interface for various types
	of sinks"""
	def __init__(self, config):
	    print("Sink initiated:", sys.exc_info()[0])

	@abstractmethod
	def logData(self, data : LogData):
	    raise NotImplementedError("logData not implemented for the Sink")