from collections import deque
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

inp = [k for k in input("Enter Input : ").split(",")]
q = QUEUE()
check = False
check2 = False
check3 = False
for l in range(0,len(inp)):
    if all(j == 'D' for j in inp ) == True :
        print("-1")
        continue
    if inp[l] == 'D':
        if not q.isEmpty():
           print(f'Pop {q.items[0]}',end=" ")
           q.deQueue()
           print(f'size in queue is {q.size()}',)
           if q.isEmpty() and check == True:
               check3 = True
               print('-1')
               continue
        else:
            if check == False:
             print('-1')
             check = True
             check2 = True
             continue


    if 'E' in inp[l]:
        E, value = inp[l].split()
        if E == 'E':
            print(f'Add {value} index is {q.size()}')
            q.enQueue(value)

if not q.isEmpty():
     print(f'Number in Queue is :  {q.showQueu()}')
else:
     print('Empty')

