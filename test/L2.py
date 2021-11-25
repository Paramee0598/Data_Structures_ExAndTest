showStr = lambda list : ' '.join(map(str, list))
from collections import deque
class Queue:
    def __init__(self, q=None):
        if q == None:
            self.items = deque()
        else:
            self.items = deque(q, len(q))
    def enQueue(self, i):
        self.items.append(i)
    def deQueueRight(self):
        self.items.pop()
    def deQueue(self):
        return self.items.popleft()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    def showQueu(self):
        Q = []
        for i in self.items:
            Q.append(i)
        return Q

inp = input("Enter choice : ")

if inp == '1':
    q1 = Queue()
    q1.enQueue(10)
    q1.enQueue(20)
    q1.enQueue(30)
    print(f'Queue data : {showStr(q1.showQueu())}')
    q1.deQueue()
    q1.enQueue(40)
    print("Size of Queue :",q1.size())
    print(f'Queue data : {showStr(q1.showQueu())}')

if inp == '2':
    q1 = Queue()
    q1.enQueue(100)
    q1.enQueue(200)
    q1.enQueue(300)
    q1.deQueue()
    print(f'Queue data : {showStr(q1.showQueu())}')
    print("Queue is Empty :", q1.isEmpty())

if inp == '3':
    q1 = Queue()
    q1.enQueue(11)
    q1.enQueue(22)
    q1.enQueue(33)
    q1.deQueue()
    q1.deQueue()
    q1.deQueue()
    if q1.isEmpty() == True:
     print(f'Empty Queue')
    print("Size of Queue :",q1.size())
    print("Queue is Empty :", q1.isEmpty())
