class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

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


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
T.showMinMax()