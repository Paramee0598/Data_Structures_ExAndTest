showStr = lambda list : ' '.join(map(str, list)) #ทำlist เป็น string
class QUEUE:
    def __init__(self):
        self.item = []
    def deQueue(self):
        return self.item.pop(0)
    def enQueue(self, i):
        self.items.append(i)
    def enQueue(self, i):
        self.item.append(i)
    def isEmpty(self):
        return self.item == []
    def peek(self):
        return self.item[0]
    def size(self):
        return len(self.item)
def prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2, x):
            if x % n == 0:
                return False

        return True
inp = [k for k in input("Enter people and time : ").split(" ")]
people = showStr(inp[0]).split(" ")
time = int(inp[1])
q = QUEUE()
i1 = QUEUE()
i2 = QUEUE()
temp = 1
# [q_main][i1][i2]
firse = True
for i in people:
    q.enQueue(i)
for p in people:
    if (q.item != []):
        q.deQueue()
        if (i1.item != [] and temp % 3 == 1):
            i1.deQueue()
            i1.enQueue(p)
            if (i2.item != [] and temp % 3 == 1 and temp % 2 == 0):
                i2.deQueue()

        else:
            if (len(i1.item) == 5):
                if (i2.item != [] and temp % 2 == 0):
                   i2.deQueue()

                i2.enQueue(p)
            else:
                i1.enQueue(p)
    else:
        i1.enQueue(p)
    print(temp,q.item,i1.item,i2.item)
    if int(temp)== int(time):
        break
    temp +=1
if int(temp) >= int(time):
     exit()


for p in i1.item:
    if (q.item == []):
            if (i1.item != [] and temp % 3 == 1):
                i1.deQueue()

                if (i2.item != [] and temp % 3 == 1 and temp % 2 == 0):
                    i2.deQueue()
            else:
                if (len(i1.item) == 5):
                    if (i2.item != [] and temp % 2 == 0):
                        i2.deQueue()
                if(len(i1.item)!=5)and temp % 2 == 0:
                    i2.deQueue()
                else:
                    if prime(temp) != True and (len(i1.item)!= 5): # ******************
                     i1.enQueue(p)
    print(temp,q.item,i1.item,i2.item)
    if int(temp) == int(time):
        exit()
    temp +=1
