# Logger


Wroking:
 1. Any process that wants log data, initializes an object of a stream(like NetBanking Stream for NetBanking logs.
 2. The stream object exposes 5 logging methods i.e.INFO, DEBUG, WARN, ERROR, FATAL.
 3. Each logging method is having its separate queue, worker and sink and it initializes on demand.
 4. At logging time, the LogData object is pushed into multiprocessing queue.(This queue is Process safe.)
 5. One or more workers based on write_mode sync or asyc keep listening on the queues for the data.
 6. While processing data, the data is sent to the specific sink based on the sink configs.

