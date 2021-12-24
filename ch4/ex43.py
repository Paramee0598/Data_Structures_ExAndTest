from collections import deque
showStr = lambda list : ' '.join(map(str, list)) #ทำlist เป็น string
class QUEUE:  # use deque
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
def ConAscii():
    q =QUEUE()
    while s.isEmpty() == False:
      if s.isEmpty() == False:
        temp = n.items[0]
        for i in range(1,(int(n.items[0]))+1):
            s.items[0] = (ord(s.items[0]))+1
            if s.items[0] > 122:
                s.items[0] = 97
            if 97 > s.items[0] > 90:
                s.items[0] = 65
            s.items[0] = chr(s.items[0])
        q.enQueue(s.items[0])
        n.deQueue()
        n.enQueue(temp)
        s.deQueue()
    return q.showQueu()
n = QUEUE()
s = QUEUE()
inp = [k for k in input("Enter String and Code : ").replace(" ","").split(",")]
SteDe = showStr(inp[0]).split(" ")
NumAsi = (showStr(inp[1]).split(" "))
for i in NumAsi:
    n.enQueue(i)
for j in SteDe:
   s.enQueue(j)
print(f'Encode message is :  {ConAscii()}')
print(f'Decode message is :  {SteDe}')




