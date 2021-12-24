class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
class BST:
    def __init__(self):
        self.root = None
        self.vmax = 0
        self.vmin = 50

    def insert(self, data):
        createNode = Node(data)
        if (self.root == None):
            self.root = createNode

        else:
            sumRoot = self.root
            while data is not None:

                if (sumRoot.data > data):
                    if (sumRoot.left == None):
                        sumRoot.left = createNode
                        if (self.vmin > sumRoot.left.data):
                            self.vmin = sumRoot.left.data

                        break
                    else:

                        sumRoot = sumRoot.left


                elif (sumRoot.data < data):

                    if (sumRoot.right == None):
                        sumRoot.right = createNode
                        if (self.vmax < sumRoot.right.data):
                            self.vmax = sumRoot.right.data

                        break
                    else:

                        sumRoot = sumRoot.right

            return self.root

    def showMinMax(self):
        print("Min :", self.vmin)
        print("Max :", self.vmax)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def multi(self, k, multiplier):  # traverse then multiply
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            sumRoot = q.dequeue()
            if sumRoot.data > k:
                sumRoot.data = sumRoot.data*multiplier
            if sumRoot.left is not None:
                q.enqueue(sumRoot.left)
            if sumRoot.right is not None:
                q.enqueue(sumRoot.right)


# T = BST()
# inpString = input('Enter Input : ')
# inpString = inpString.replace('/',' ')
# inp = [int(i) for i in inpString.split()]
# k = inp[-1]
# inp.remove(inp[-1])
# for i in inp:
#     root = T.insert(i)
# T.printTree(root)
# print("--------------------------------------------------")
# T.multi(k, 3)
# T.printTree(root)
T = BST()
inp = input('Enter Input : ').split('/')
lst = list(map(int, inp[0].split()))
k = int(inp[1])
root = None
for item in lst:
      root = T.insert(item)
T.printTree(root)
print('--------------------------------------------------')
T.multi(k, 3)
T.printTree(root)