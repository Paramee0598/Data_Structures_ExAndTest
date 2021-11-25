class Stack:

    def __init__(self):
        self.item = []

    def push(self, i):
        self.item.append(i)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def bottom(self):
        return self.item[0]

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def str (self):
        temp = list(map(str,self.item))
        temp = " ".join(temp)
        return f"Data in Stack is : {temp}"

    def showQueu(self):
        Q = []
        for i in self.item:
            Q.append(i)
        return Q

s1 = Stack()
inp = int(input("Enter choice : "))

if(inp==1):

    s1.push(10)
    s1.push(20)
    print(s1.str())
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())

elif(inp==2):

    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1.str())
    print("Stack is Empty :",s1.isEmpty())

elif(inp==3):

    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1.str())
    print("Stack size :",s1.size())