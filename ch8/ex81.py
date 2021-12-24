class Node:
    def __init__(self, new_item, frequency):
        self.item = new_item
        self.frequency = frequency
        self.left = None
        self.right = None

    def __len__(self):
        return self.frequency


class Stack:
    def __init__(self):
        self.items = []

    def push(self, new_item):
        self.items.append(new_item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def deq(self):
        if self.items:
            return self.items.pop(0)
        return None

    def top(self):
        if self.items:
            return self.items[-1]
        return None

    def head(self):
        if self.items:
            return self.items[0]
        return None


class Huffman:
    def __init__(self):
        self.root = None
        self.items = []
        self.w = {}

    def prepare(self, inputlist):
        l = sorted(inputlist)
        dic = {i: l.count(i) for i in l}
        dic = dict(sorted(dic.items(), key=lambda x: x[1]))
        keys = list(dic.keys())
        sort = [Node(key, dic[key]) for key in keys[::-1]]
        while len(sort):
            self.items.append(sort[0])
            for j in sort[1:]:
                if sort[0].frequency == j.frequency:
                    self.items.append(j)
                    sort.remove(j)
            sort.remove(sort[0])

    # def insert(self):
    #     s = Stack()
    #     s.items = self.items
    #     for _ in range(len(s.items)-1):
    #         first = s.pop()
    #         second = s.top()
    #         if first.frequency <= second.frequency:
    #             print(first.item,first.frequency,second.item,second.frequency)
    #             s.pop()
    #             r = Node('*',first.frequency + second.frequency)
    #             r.left = first
    #             r.right = second
    #             if not s.items:
    #                 s.push(r)
    #             for i in range(len(s.items)):
    #                 if r.frequency > s.items[i].frequency:
    #                     s.items.insert(i,r)
    #                     break
    #                 if i == len(s.items)-1:
    #                     s.push(r)
    #         else:
    #             print('else')
    #     self.root = s.head()

    # def insert(self):
    #     s = Stack()
    #     t = Stack()
    #     s.items = self.items
    #     while s.items:
    #         print([i.item for i in s.items],[i.item for i in t.items])
    #         if t.items:
    #             s.items = t.items[::-1] + s.items
    #             t.items.clear()

    #         # if len(s.items) == 1 and len(t.items) == 1:
    #         #     break
    #         first = s.pop()
    #         second = s.top()
    #         if first.frequency <= second.frequency:
    #             # print(first.item,first.frequency,second.item,second.frequency)
    #             s.pop()
    #             r = Node('*',first.frequency + second.frequency)
    #             r.left = first
    #             r.right = second
    #             # if not s.items:
    #             t.push(r)
    #             # for i in range(len(s.items)):
    #             #     if r.frequency > s.items[i].frequency:
    #             #         s.items.insert(i,r)
    #             #         break
    #             #     if i == len(s.items)-1:
    #             #         s.push(r)
    #         else:
    #             # print(first.item)
    #             t.push(first)
    #             # first = s.pop()
    #             # second = s.top()
    #             # while
    #             # print('else')
    #         print([i.item for i in s.items],[i.item for i in t.items])
    #     if t.items:
    #         s.items = t.items[::-1] + s.items
    #         t.items.clear()
    #     self.root = s.head()

    # def insert(self):
    #     s = Stack()
    #     t = Stack()
    #     s.items = self.items
    #     while len(s.items) != 1 or t.items:
    #         print([i.item for i in s.items],[i.item for i in t.items])
    #         first = s.pop()
    #         second = s.top()
    #         print([i.item for i in s.items],[i.item for i in t.items])
    #         if first.frequency <= second.frequency:
    #             print('if first.frequency <= second.frequency:')
    #             s.pop()
    #             r = Node('*',first.frequency + second.frequency)
    #             r.left = first
    #             r.right = second
    #             t.push(r)
    #             print([i.item for i in s.items],[i.item for i in t.items])
    #         if len(s.items) == 1 and t.items:
    #             print('if len(s.items) == 1 and t.items:')
    #             check = True
    #             print(check)
    #             print([i.item for i in s.items],[i.item for i in t.items])
    #             for _ in t.items[::-1]:
    #                 if s.head().frequency >= t.top().frequency and check:
    #                     s.push(s.deq())
    #                     check = False
    #                 s.push(t.pop())
    #             print(check)
    #             if check:
    #                 s.push(s.deq())
    #             print([i.frequency for i in s.items],[i.frequency for i in t.items])

    #         if not s.items and t.items:
    #             print('if not s.items and t.items:')
    #             s.items = t.items[::-1] + s.items
    #             t.items.clear()
    #             print([i.frequency for i in s.items],[i.frequency for i in t.items])

    #     self.root = s.head()

    # def insert(self):
    #     s = Stack()
    #     t = Stack()
    #     s.items = self.items

    #     while len(s.items) != 1 or t.items:
    #         settop = Node(None,0)
    #         oddelement = [s.items[i] for i in range(len(s.items)-1,0,-1) if s.items[i].frequency == s.top().frequency ]
    #         print(len(oddelement),[i.item for i in oddelement],(len(oddelement)%2 == 1 and len(oddelement) != 1))
    #         if len(oddelement)%2 == 1 and len(oddelement) != 1:
    #             settop = oddelement[-1]
    #             print()
    #         # print([i.item for i in s.items],[i.item for i in t.items])
    #         first = s.pop()
    #         second = s.top()
    #         print(first.item,settop.item)
    #         if first is settop:
    #             s.push(first)
    #         # print([i.item for i in s.items],[i.item for i in t.items])
    #         if first.frequency <= second.frequency:
    #             # print('if first.frequency <= second.frequency:')
    #             s.pop()
    #             r = Node('*',first.frequency + second.frequency)
    #             r.left = first
    #             r.right = second
    #             t.push(r)
    #             # print([i.item for i in s.items],[i.item for i in t.items])
    #         if len(s.items) == 1 and t.items:
    #             # print('if len(s.items) == 1 and t.items:')
    #             check = True
    #             print(check,s.head().frequency, t.top().frequency)
    #             # print([i.item for i in s.items],[i.item for i in t.items])
    #             for _ in t.items[::-1]:
    #                 if s.head().frequency >= t.top().frequency and check:
    #                     s.push(s.deq())
    #                     check = False
    #                 s.push(t.pop())
    #             print(check)
    #             if check:
    #                 s.push(s.deq())
    #             # print([i.frequency for i in s.items],[i.frequency for i in t.items])

    #         if not s.items and t.items:
    #             # print('if not s.items and t.items:')
    #             s.items = t.items[::-1] + s.items
    #             t.items.clear()
    #             # print([i.frequency for i in s.items],[i.frequency for i in t.items])
    #     self.root = s.head()

    # def insert(self):
    #     # s = Stack()
    #     # t = Stack()
    #     old_list = self.items
    #     new_list = []
    #     # s.items = self.items
    #     for i in range(len(self.items)):
    #         if old_list[i].fre

    # def insert(self):
    #     # print([i.item for i in self.items])

    #     s = Stack()
    #     t = Stack()
    #     s.items = self.items
    #     # print([[i.item, i.frequency] for i in s.items])

    #     first = s.pop()
    #     second = s.pop()
    #     new_node = Node('*',first.frequency + second.frequency)
    #     new_node.left = first
    #     new_node.right = second

    #     # if first.frequency < second.frequency:
    #     #     s.items = [i for i in s.items if i.frequency >= new_node.frequency] + [new_node] + [i for i in s.items if i.frequency < new_node.frequency]
    #     #     # s.push(new_node)
    #     #     self.items = s.items
    #     #     # print([i.item for i in s.items])
    #     #     return
    #     # elif first.frequency == second.frequency:
    #     #     if first.item == '*' and second.item == '*':
    #     #         s.items = [i for i in s.items if i.frequency >= new_node.frequency] + [new_node] + [i for i in s.items if i.frequency < new_node.frequency]
    #     #         self.items = s.items
    #     #         return
    #     #     elif first.item != '*' and second.item != '*':
    #     #         s.items = [i for i in s.items if i.frequency >= new_node.frequency] + [new_node] + [i for i in s.items if i.frequency < new_node.frequency]
    #     #         self.items = s.items
    #     #         return None
    #     # s.items = [i for i in s.items if i.frequency >= new_node.frequency] + [new_node] + [i for i in s.items if i.frequency < new_node.frequency]
    #     # print([[i.item, i.frequency] for i in s.items])
    #     # # print([i.item for i in s.items])

    #     # if new_node.item == s.items[-1].item and new_node.frequency == s.items[-1].frequency:
    #     #     self.items = self.items + [new_node]
    #     #     print([i.item for i in s.items])

    #     # if new_node.frequency in [i.frequency for i in self.items] and new_node.item == '*':
    #     l = []
    #     equal_new_node = [i for i in self.items if i.frequency == new_node.frequency]
    #     haveaphabet = [i for i in equal_new_node if i.item != '*']
    #     # self.items = [i for i in self.items if i.frequency >= new_node.frequency] + [new_node] + [i for i in self.items if i.frequency < new_node.frequency]
    #     l += [i for i in self.items if i.frequency > new_node.frequency]
    #     l += [i for i in self.items if i.frequency == new_node.frequency and i.item != '*']
    #     l += [new_node]
    #     l += [i for i in self.items if i.frequency == new_node.frequency and i.item == '*']
    #     l += [i for i in self.items if i.frequency < new_node.frequency]
    #     # print(l)
    #     self.items = l
    #     # if
    #     print([i.item for i in haveaphabet])
    #     print([i.item for i in self.items])

    #     # new_list = []
    #     # if len(s.items) == 0:
    #     #     new_list.append(new_node)
    #     # for i in range(len(s.items)):
    #     #     if s.items[i].frequency < new_node.frequency:
    #     #         new_list += s.items[0:i] + [new_node] + s.items[i::]
    #     #         break
    #     #     if s.items[i].frequency == new_node.frequency and s.items[i].item == '*' and new_node.item == '*':
    #     #         new_list += s.items[0:i] + [new_node] + s.items[i::]
    #     #         break

    #     #         # if s.items[i].item != '*' and new_node.item != '*':
    #     #         #     if ord(s.items[i].item) < ord(new_node.item):
    #     #         #         new_list += s.items[0:i] + [new_node] + s.items[i::]
    #     #         #         break
    #     #         # elif s.items[i].item == '*' and new_node.item == '*':
    #     #         #     new_list += s.items[0:i] + [new_node] + s.items[i::]
    #     #         #     break

    #     #     if i == len(s.items)-1:
    #     #         new_list = s.items + [new_node]
    #     #         break
    #     # self.items = new_list
    #     # print([[i.item, i.frequency] for i in self.items])

    #     # return new_list

    def insert(self):
        new_node = Node('*', self.items[-1].frequency + self.items[-2].frequency)
        new_node.left = self.items.pop()
        new_node.right = self.items.pop()
        l = []
        l += [i for i in self.items if i.frequency > new_node.frequency]
        l += [i for i in self.items if i.frequency == new_node.frequency and i.item != '*']
        l += [new_node]
        l += [i for i in self.items if i.frequency == new_node.frequency and i.item == '*']
        l += [i for i in self.items if i.frequency < new_node.frequency]
        self.items = l

    def preorder(self, node, level=0):
        if node:
            self.preorder(node.right, level + 1)
            print('', '     ' * level + node.item)
            self.preorder(node.left, level + 1)

    def huffman_code(self, node, bit=''):
        d = dict()
        if node.item != '*':
            return {node.item: bit}
        d.update(self.huffman_code(node.right, bit + '1'))
        d.update(self.huffman_code(node.left, bit + '0'))
        return d


token = [i for i in input('Enter Input : ')]
t = Huffman()
t.prepare(token)
while len(t.items) > 1:
    t.insert()
t.root = t.items[0]
d = t.huffman_code(t.root)
print(d)
t.preorder(t.root, 0)
print('', end='')
print('Encoded! :', ''.join(d[i] for i in token))
