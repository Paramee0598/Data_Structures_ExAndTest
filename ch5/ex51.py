class SinglyLinkedListNoDummy:  # ทำงานเหมือนกับ List (อ้าง อินเด็กซ์แบบเดียวกัน)
    class Node:  # โหนดเก็บข้อมูล
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):  # แสดงข้อมูลทุกตัวใน linked list
        #s = 'linked i : '
        s = ''
        p = self.head
        while p != None:
            s += str(p.data)
            p = p.next
        return " <- ".join(s) ####

    def __len__(self):  # เพิ่ม เมื่อ เติมข้อมูล  ลด เมื่อ นำข้อมูลออก
        return self.size

    def isEmpty(self):  # ตรวจสอบว่ามีข้อมูลใน linked list ไหม
        return self.size == 0  # len(self) == 0

    def indexOf(self, data):  # หา อินเด็กของข้อมูลว่าอยู่ที่ตำแหน่งใด
        p = self.head
        for i in range(len(self)):
            if p.data == data:
                return i
            p = p.next
        return -1

    def isIn(self, data):  # ตรวจสอบว่าใน linked list นี้ มีข้อมูลตัวนี้ไหม
        return self.indexOf(data) >= 0

    def nodeAt(self, i):  # หาค่าตำแหน่งของโหนด เทียบกับ อินเด็กซ์
        p = self.head
        for j in range(0, i):
            p = p.next
        return p

    def append(self, data):  # เพิ่ม ข้อมูล ไปที่ด้านท้ายของ linked list
        if self.head is None:
            p = self.Node(data)
            self.head = p
            # self.head = self.Node(i,None)
            self.tail = p
            self.size += 1
        else:  # เพิ่ม ในกรณีที่ไม่ใช่ Node แรก
            self.addTail(data)
            # self.insertAfter(len(self)-1,i)   #len(self) = จำนวนสมาชิก - 1 คือ index
            # self.tail = self.nodeAt(len(self)-1)

    def insertAfter(self, i, data):  # เพิ่ม ข้อมูล ในสายข้อมูลที่มีอยู่แล้ว (ตำแหน่งที่จะinsertข้างหลัง,ค่าที่จะinsert)
        q = self.nodeAt(i)
        p = self.Node(data)
        # self.tail = p if q == self.tail else self.tail
        ##if q == self.tail :
        ##  self.tail = p
        p.next = q.next
        q.next = p
        # q.next = self.Node(i,q.next)
        self.size += 1

    def addTail(self, data):
        q = self.tail
        p = self.Node(data)
        q.next = p
        self.tail = p
        self.size += 1

    def removeTail(self):
        if self.size > 0:
            q = self.nodeAt(len(self) - 2)
            self.tail = q
            q.next = None
            self.size -= 1

    def deleteAfter(self, i):  # ลบ โหนดข้อมูล ในสายข้อมูลที่มีอยู่แล้ว
        if self.size > 0:  # len(self)
            q = self.nodeAt(i)
            # if i == len(self)-2 :
            #  self.tail = q
            q.next = q.next.next
            self.size -= 1

    def delete(self, i):  # ลบข้อมูลที่ อินเด็กซ์ที่กำหนด
        if self.size > 0:
            if i == 0:  # ลบตัวแรก
                self.head = self.head.next
                self.size -= 1
            elif i == len(self) - 1:
                self.removeTail()
            else:
                self.deleteAfter(i - 1)  # ลบตัวก่อนหน้า

    def removeData(self, data):  # ลบข้อมูลใน linked list
        if self.isIn(data):
            self.deleteAfter(self.indexOf(data) - 1)

    def addHead(self, data):
        if self.isEmpty():
            p = self.Node(data)
            self.head = p
            # self.head = self.Node(i,None)
            self.size += 1
        else:
            p = self.Node(data, self.head)
            self.head = p
            self.size += 1

    def moveToFront(self):
        tmp = self.head
        sec_last = None


        if not tmp or not tmp.next:
            return


        while tmp and tmp.next:
            sec_last = tmp
            tmp = tmp.next


        sec_last.next = None


        tmp.next = self.head
        self.head = tmp
def Locomotive():
    l = SinglyLinkedListNoDummy()
    print(" *** Locomotive ***")
    inp = [k for k in input("Enter Input : ").split(" ")]
    for i in inp:
        l.append(i)
    print(f'Before : {l}')
    i = l.size - l.indexOf("0")
    for o in range(i):
        l.moveToFront()
    print(f'After : {l}')
Locomotive()
