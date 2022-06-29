class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def preorder(root):

    if root:
        # Traverse Root
        print(str(root.val) + "->", end=" ")
        # Traverse left
        preorder(root.left)
        # Traverse Right
        preorder(root.right)


def inorder(root):
    if root:
        # Traverse Left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end=" ")
        # Traverse Right
        inorder(root.right)


def postorder(root):
    if root:
        # Traverse Left
        postorder(root.left)
        # Traverse Right
        postorder(root.right)
        # Traverse Root
        print(str(root.val) + "->", end=" ")


root = Node(2)
root.left = Node(7)
root.right = Node(9)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(5)
root.left.right.right = Node(10)
root.right.right = Node(8)
root.right.right.left = Node(3)
root.right.right.right = Node(4)


print("Preorder Traversal")
preorder(root)

print("\nInorder Traversal")
inorder(root)

print("\nPostorder Traversal")
postorder(root)




