class Treenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
        if node is None:
            return
        inOrderTraversal(node.left)
        print(node.data, end=", ")
        inOrderTraversal(node.right)

root= Treenode(13)
node7 = Treenode(7)
node15 = Treenode(15)
node3 = Treenode(3)
node8 = Treenode(8)
node14 = Treenode(14)
node19 = Treenode(19)
node18 = Treenode(18) 


root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.left = node19

node19.left = node18


# traversal
inOrderTraversal(root)



         

