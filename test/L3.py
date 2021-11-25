class LinkedList:
    class Node :
        def __init__(self, i, next = None) :
            self.data = i
            if next is None :
                self.next = None
            else :
                self.next = next

        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self) :
        s = 'Linked i : '
        pn = self.head
        while pn != None :
            s += str(pn.data)+' '
            pn = pn.next
        return s

    def __len__(self) :
        return self.size

    def append(self, i):
        p = self.Node(i)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p
            self.tail =p
        self.size += 1

    def isEmpty(self) :
        return self.size == 0

    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def removeDup(self):
        if not self.isEmpty():
            temp = {}
            ph = None
            b = self.head
            while b is not None:
                if temp.get(b.data,0) == 0:
                    temp[b.data] = 1
                    ph = b
                    b = b.next
                else:
                    if b.next is not None:
                        ph.next = b.next
                        b.next = None
                        b = ph.next
                    else:
                        ph.next = None
                        b = None

inp = [int(i) for i in input('Enter numbers : ').split()]

l = LinkedList()
for i in inp:
  l.append(i)
print("Linkedlist Before removeDuplicate")
print(l.__str__())
print("Linkedlist After removeDuplicate")
l.removeDup()
print(l.__str__())