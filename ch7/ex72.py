class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right

    def __str__(self):
        return str(self.data)

    def getData(self):         # accessor
        return self.data

    def getRoot(self):  # accessor
        return self.left + self.right

    def getLeft(self):         # accessor
        return self.left

    def getRight(self):        # accessor
        return self.right

    def setData(self, data):   # mutator
        self.data = data

    def setLeft(self, left):   # mutator
        self.left = left

    def setRight(self, right): # mutator
        self.right = right

class BST:
    def __init__(self, root=None):
        self.root = None if root is None else root     #ตัวเยอะ
        self.getRoot = 0

    def insert(self, data):
        createNode = Node(data)
        if self.root is None:
            self.root = createNode
        else:
            calNode = self.root
            while data is not None:
              if data < calNode.getData():
                 if calNode.left is None :
                     calNode.left = createNode
                     self.getRoot = self.getRoot +1
                     break
                 else:
                   calNode = calNode.left

              if data > calNode.getData():
                if calNode.right is None:
                    calNode.right = createNode
                    self.getRoot = self.getRoot + 1
                    break
                else:
                  calNode = calNode.right

        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def height(obj):
    if (obj == None):
        return -1

    numRootLeft = height(obj.left) + 1
    numRootRight = height(obj.right) + 1

    return max(numRootLeft, numRootRight)
tree = BST()
arr = list(map(int, input("Enter Input : ").split()))

for e in arr:
    tree.insert(e)

print(f'Height of this tree is : {height(tree.root)}')
