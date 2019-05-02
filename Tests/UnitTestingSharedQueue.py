from modules.Queues.SharedBaseQueue import SharedBaseQueue

SBQ = SharedBaseQueue('q1')

print("number of queues: ", SBQ.getCurrentNumberOfQueues())

print("TESTING ADDITION OF QUEUES")
SBQ.addQueues(2)
print("number of queues: ", SBQ.getCurrentNumberOfQueues())

## Adding an element to a queue
q0 = SBQ.getQueue()
q0.put(0)
q0.get()

SBQ.addQueues(3)
print("number of queues: ", SBQ.getCurrentNumberOfQueues())

# use of modulus
q = SBQ.getQueue(3)
q = SBQ.getQueue(100)
q = SBQ.getQueue(-11)


q = SBQ.getQueue(0)
q.put(0)
q = SBQ.getQueue(4) # 4%4 = 0 so points to same queue
q.get()