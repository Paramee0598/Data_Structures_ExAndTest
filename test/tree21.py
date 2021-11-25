class Tree_Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def list_to_bst(listNum):
    if len(listNum) >1:
        mid = int(len(listNum) / 2)
        node = Tree_Node(listNum[mid])
        if mid != 0:
            temp = list_to_bst(listNum[:mid])
            node.left = temp
        if mid != len(listNum)-1:
            temp = list_to_bst(listNum[mid + 1:])
            node.right = temp
        return node
    else:
        node = Tree_Node(listNum[0])
        return node

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

def printBST(node,level = 0):
    if node != None:
        printBST(node.right, level + 1)
        print('     ' * level, node.val)
        printBST(node.left, level + 1)

list_nums = sorted([int(item) for item in input("Enter list : ").split()])
result = list_to_bst(list_nums)

print("\nList to a height balanced BST : ")
print(preOrder(result))
print("\nBST model : ")
printBST(result)