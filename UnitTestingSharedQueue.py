from BaseSharedQueue import BaseSharedQueue

sq = BaseSharedQueue('q1')

print("number of queues: ", sq.getCurrentNumberOfQueues())

print("TESTING ADDITION OF QUEUES")
sq.addQueues(2)
print("number of queues: ", sq.getCurrentNumberOfQueues())

## Adding an element to a queue
q0 = sq.getQueue()
q0.put(0)
q0.get()

sq.addQueues(3)
print("number of queues: ", sq.getCurrentNumberOfQueues())

# use of modulus
q = sq.getQueue(3)
q = sq.getQueue(100)
q = sq.getQueue(-11)


q = sq.getQueue(0)
q.put(0)
q = sq.getQueue(4) # 4%4 = 0 so points to same queue
q.get()