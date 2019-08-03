import Queue

class BinarySearchTree(object):
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def search_tree(tree,key):
    if not tree:
        return
    elif key==tree.value:
        return tree
    elif key<tree.value:
        return search_tree(tree.left,key)
    else:
        return search_tree(tree.right,key)

def tree_height(tree):
    if not tree:
        return 0
    else:
        return 1 + max(tree_height(tree.left),tree_height(tree.right))

def tree_size(tree):
    if not tree:
        return 0
    else:
        return 1 + tree_size(tree.left) + tree_size(tree.right)

class DepthFirst(object):
    def in_order_traversal(self):
        if not self:
            return
        else:
            DepthFirst.in_order_traversal(self.left)
            print(self.value)
            DepthFirst.in_order_traversal(self.right)
    def pre_order_traversal(self):
        if not self:
            return
        else:
            print(self.value)
            DepthFirst.pre_order_traversal(self.left)
            DepthFirst.pre_order_traversal(self.right)
    def post_order_traversal(self):
        if not self:
            return
        else:
            DepthFirst.post_order_traversal(self.left)
            DepthFirst.post_order_traversal(self.right)
            print(self.value)

class BreadthFirst(object):
    def level_traversal(self):
        if not self:
            return
        else:
            q=Queue.Queue()
            q.enqueue(self)
            while not q.is_empty():
                node=q.dequeue()
                if node.left:
                    q.enqueue(node.left)
                if node.right:
                    q.enqueue(node.right)




# Tree Creation
t12=BinarySearchTree(12)
t10=BinarySearchTree(10)
t11=BinarySearchTree(11,t10,t12)
t9=BinarySearchTree(9,None,t11)
t7=BinarySearchTree(7)
t8=BinarySearchTree(8,t7,t9)
t5=BinarySearchTree(5)
t6=BinarySearchTree(6,t5,t8)
t1=BinarySearchTree(1)
t3=BinarySearchTree(3)
t2=BinarySearchTree(2,t1,t3)
t4=BinarySearchTree(4,t2,t6)

#Function Testing
search_tree(t4,7).value
print(search_tree(t4,13))
print(search_tree(t4,0))
search_tree(t4,9).value
search_tree(t4,1).value
search_tree(t4,12).value
search_tree(t4,3).value
search_tree(t4,4).value
search_tree(t4,1).value
search_tree(t4,11).value
tree_height(t4)
tree_height(t2)
tree_height(t12)
tree_height(t9)
tree_height(t6)
tree_height(t11)
tree_size(t4)
tree_size(t12)
tree_size(t1)
tree_size(t11)
tree_size(t8)
DepthFirst.in_order_traversal(t4)
DepthFirst.in_order_traversal(t6)
DepthFirst.pre_order_traversal(t4)
DepthFirst.pre_order_traversal(t9)
DepthFirst.pre_order_traversal(t1)
DepthFirst.post_order_traversal(t4)
DepthFirst.post_order_traversal(t12)
DepthFirst.post_order_traversal(t8)
BreadthFirst.level_traversal(t4)
BreadthFirst.level_traversal(t12)
