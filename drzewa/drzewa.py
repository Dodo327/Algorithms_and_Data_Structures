class Node:
    def __init__(self, value, right, left):
        self.value = value
        self.right = right
        self.left = left
        


#T(n) = 2*T(n-1) + 1
def inOrder(root):
    if root is None:
        return
    
    inOrder(root.right)
    print((root.value))
    inOrder(root.left)
    
def preOrder(root):
    if root is None:
        return
    
    print((root.value))
    preOrder(root.right)
    preOrder(root.left)
    
def postOrder(root):
    if root is None:
        return
    
    postOrder(root.right)
    postOrder(root.left)
    print((root.value))
