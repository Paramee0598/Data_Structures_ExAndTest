class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, data):
        p = Node(data)
        if (self.root == None):
            self.root = p

        else:
            sumRoot = self.root
            while data != None:
                if (sumRoot.data > data):
                    if (sumRoot.left == None):
                        sumRoot.left = p
                        break
                    else:
                        sumRoot = sumRoot.left

                elif (sumRoot.data < data):
                    if (sumRoot.right == None):
                        sumRoot.right = p
                        break
                    else:
                        sumRoot = sumRoot.right
            return self.root


def height(obj):
    if (obj == None):
        return -1

    numRootLeft = height(obj.left) + 1
    numRootRight = height(obj.right) + 1

    return max(numRootLeft, numRootRight)


print(" *** Binary Search Tree Height ***")
tree = BinarySearchTree()
arr = list(map(int, input("Enter Input : ").split()))

for e in arr:
    tree.create(e)

print("Height = ", height(tree.root), end="\n\n")