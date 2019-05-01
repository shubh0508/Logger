import sys
from LogData import LogData

"""This class works as an interface for various transaction"""
class Sink():

    def __init__(self, config):
        print("Unexpected error at Sink constructor :", sys.exc_info()[0])

    def logData(self, data : LogData):
        raise NotImplementedError("Predict Not implemented for the Model")