class LinkedList:
    class Node:
        def __init__(self, i, next=None):
            self.data = i
            if next is None:
                self.next = None
            else:
                self.next = next

        def __str__(self):
            return str(self.data)

    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None:
                t = t.next
                self.size += 1
            self.tail = t

    def __len__(self):
        return self.size

    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p
            self.tail = p
        self.size += 1

    def removeHead(self):
        if self.head == None: return
        if self.head.next == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def isEmpty(self):
        return self.size == 0

    def nodeAt(self, i):
        p = self.head
        for j in range(i):
            p = p.next
        return p

    def contentEquivalence(self, inputList):
        if len(self) != len(inputList):
            return False
        s1 = set()
        s2 = set()
        for i in range(len(self)):
            s1.add(self.nodeAt(i).data)
        for i in range(len(inputList)):
            s2.add(inputList.nodeAt(i).data)
        return s1 == s2


inp = input('List1,List2 : ').split(',')
list1 = inp[0].split()
list2 = inp[1].split()
l1 = LinkedList() ; l2 = LinkedList()
for i in list1:
    l1.append(i)
for i in list2:
    l2.append(i)
print(f'List1 content Equivalence List2 : {str(l1.contentEquivalence(l2))}')