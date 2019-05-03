# Logger


##Wroking:
  1. Any process that wants log data, initializes an object of a stream(like NetBanking Stream for NetBanking logs.
  2. The stream object exposes 5 logging methods i.e.INFO, DEBUG, WARN, ERROR, FATAL.
  3. Each logging method is having its separate queue, worker and sink and it initializes on demand.
  4. At logging time, the LogData object is pushed into multiprocessing queue.(This queue is Process safe.)
  5. One or more workers based on write_mode sync or asyc keep listening on the queues for the data.
  6. While processing data, the data is sent to the specific sink based on the sink configs.

PSQL Database Table:
    CREATE TABLE log_table(
     id serial PRIMARY KEY,
     level VARCHAR (10) NOT NULL,
     mmessage_namespace VARCHAR (50) NOT NULL,
     message_content TEXT NOT NULL,
     log_time TIMESTAMP NOT NULL,
     added_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );


##Running Environment:
  1. Tested on Jupyter notebook. Flask App can also be used.
  2. PSQL Database server is used for Testing the logging.
  3. Fetches settings of streams from Settings/settings.json
  4. For running Tests, just run '%run Tests/TestFile.py'
  
##Further Works:
  1. Proper Managers for Queues and Workers.
  2. Removing dependency of Sink on LogData Object by introducing a SinkObjectInterface.
  3. Using unittest python library for TestCases and making them a part of build process using single command.
  4. Testing the Cost and performance by using Redis server for temporary queuing.
  

