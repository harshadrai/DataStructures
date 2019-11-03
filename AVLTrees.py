'''
An AVL Tree is a Binary Search Tree that remains balanced (complete)
by inserting and deleting nodes and merging and splitting trees
'''


class Node(object):
    def __init__(self,key=None,left=None,right=None,parent=None):
        self.key=key
        self.left=left
        self.right=right
        self.parent=parent
        self.height=1
        self.size=1

class AVL_Tree(Node):
    def __init__(self,key=None):
        self.root=Node(key)
    def find(self,k):
        R=self.root
        if k==R.key:
            return R
        elif k<R.key:
            if R.left:
                return R.left.find(k)
            return R
        elif k>R.key:
            if R.right:
                return R.right.find(k)
            return R
    def next(self,N):
        if N.right:
            R=N.right
            while R.left:
                R=R.left
            return R
        else:
            P=N.parent
            while P and P.key<N.key:
                P=P.parent
            return P
    def previous(self,N):
        if N.left:
            L=N.left
            while L.right:
                L=L.right
            return L
        else:
            P=N.parent
            while P and P.key>N.key:
                P=P.parent
            return P
    def range_search(self,x,y):
        L=[]
        N=self.find(x)
        while N.key<=y:
            if N.key>=x:
                L.append(N)
            N=next(N)
        return L
    def nearest_neighbor(self,x):
        N=self.find(x)
        if x==N.key:
            L=self.previous(N)
            R=self.next(N)
            return (L,R)
        elif x<N.key:
            L=self.previous(N)
            return (L,N)
        elif x>N.key:
            R=self.next(N)
            return (N,R)
    def insert(self,k):
        R=self.root
        N=Node(k)
        if not R:
            R=N
        else:
            P=self.find(k)
            if k==P.key:
                return
            elif k<P.key:
                P.left=N
            elif k>P.key:
                P.right=N
            N.parent=P
    def delete(self,N):
        P=N.parent
        if P:
            if not N.right:
                if N.left:
                    N.left.parent=P
                if P.right.key==N.key:
                    P.right=N.left
                else:
                    P.left=N.left
            else:
                X=self.next(N)     # X has no left child
                X.parent.left=X.right
                X.parent=P
                X.left=N.left
                X.right=N.right
                if P.right.key==N.key:
                    P.right=X
                else:
                    P.left=X
        else:
            return
    def rotate_right(self,X):
        P=X.parent
        A=X.left
        B=A.right
        A.right=X
        A.parent=P
        X.parent=A
        if B:
            X.left=B
            B.parent=X
        if P and P.right.key==X.key:
            P.right=A
        elif P and P.left.key==X.key:
            P.left=A
    def rotate_left(self,X):
        P=X.parent
        A=X.right
        B=A.left
        A.left=X
        X.parent=A
        A.parent=P
        if B:
            X.right=B
            B.parent=X
        if P and P.right.key==X.key:
            P.right=A
        elif P and P.left.key==X.key:
            P.left=A
    def avl_insert(self,k):
        self.insert(k)
        N=self.find(k)
        self.rebalance(N)
    def rebalance(self,N):
        P=N.parent
        left_height=N.left.height if N.left else 0
        right_height=N.right.height if N.right else 0
        if left_height>right_height+1:
            self.rebalance_right(N)
        elif right_height>left_height+1:
            self.rebalance_left(N)
        self.adjust_height(N)
        if P:
            self.rebalance(P)
    def adjust_height(self,N):
        left_height=N.left.height if N.left else 0
        right_height=N.right.height if N.right else 0
        N.height=1+max(left_height,right_height)
    def rebalance_right(self,N):
        M=N.left
        M_left_height=M.left.height if M.left else 0
        M_right_height=M.right.height if M.right else 0
        if M_right_height>M_left_height:
            self.rotate_left(M)
        self.rotate_right(N)
        # adjust_height(N.right)
        self.adjust_height(N)
        self.adjust_height(M)
        X=M.parent
        if X:
            self.adjust_height(X)
            if not X.parent:
                self.root=X
        else:
            self.root=M
    def rebalance_left(self,N):
        M=N.right
        M_left_height=M.left.height if M.left else 0
        M_right_height=M.right.height if M.right else 0
        if M_left_height>M_right_height:
            self.rotate_right(M)
        self.rotate_left(N)
        # adjust_height(N.left)
        self.adjust_height(N)
        self.adjust_height(M)
        X=M.parent
        if X:
            self.adjust_height(X)
            if not X.parent:
                self.root=X
        else:
            self.root=M

n1=AVL_Tree(1)
n1.avl_insert(2)
