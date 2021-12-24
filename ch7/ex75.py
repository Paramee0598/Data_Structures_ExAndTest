class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.vmax = 0
        self.vmin = 200

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
    # def create(self, val):
    #     if self.root == None:
    #         self.root = Node(val)
    #
    #     else:
    #         current = self.root
    #         while True:
    #             if val < current.data:
    #                 if current.left:
    #                     current = current.left
    #                 else:
    #                     current.left = Node(val)
    #                     break
    #             elif val > current.data:
    #                 if current.right:
    #                     current = current.right
    #                 else:
    #                     current.right = Node(val)
    #                     break
    #             else:
    #                 break


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


def checkpos(r, data):
    t_tree = r
    while True:
        if (t_tree.data > data and t_tree.left != None):
            # print("in 1")
            if (t_tree.left.data == data):
                print(t_tree.data)
                break

            else:
                # print("finnish 1")
                t_tree = t_tree.left


        elif (t_tree.data < data and t_tree.right != None):
            # print("in 2")
            if (t_tree.right.data == data):
                #print(f'this left {t_tree.left.data}')
                #print(f'this data {data}')
                #print(f'this tree data {t_tree.data}')
                #print(f'this right {t_tree.right.data}')
                #print(f'this left {t_tree.left.data}')
                if t_tree.data < t_tree.right.data and all(int(data) >= int(i) for i in inp) is True:
                   print("Leaf")
                #if t_tree.data >= t_tree.right.data:
                else:
                   print("Inner")
                break

            else:
                # print("finnish 2")
                t_tree = t_tree.right

        elif (t_tree.data == data):
            print("Root")
            break

        else:
            print("Not exist")
            break

#300 100 70 200 34 80 300
tree = BinarySearchTree()
inp = [i for i in input('Enter Input : ').split()]
selectNum = inp[0]

inp.pop(0)
# print(data)
for e in inp:
    tree.insert(int(e))
printTree90(tree.root)
checkpos(tree.root, int(selectNum))