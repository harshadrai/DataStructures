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

def find(k,R):
    if k==R.key:
        return R
    elif k<R.key:
        if R.left:
            return find(k,R.left)
        return R
    elif k>R.key:
        if R.right:
            return find(k,R.right)
        return R

def next(N):
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

def previous(N):
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

def range_search(x,y,R):
    L=[]
    N=find(x,R)
    while N.key<=y:
        if N.key>=x:
            L.append(N)
        N=next(N)
    return L

def nearest_neighbor(x,R):
    N=find(x,R)
    if x==N.key:
        L=previous(N)
        R=next(N)
        return (L,R)
    elif x<N.key:
        L=previous(N)
        return (L,N)
    elif x>N.key:
        R=next(N)
        return (N,R)

def insert(k,R):
    N=Node(k)
    if not R:
        R=N
    else:
        P=find(k,R)
        if k==P.key:
            return R
        elif k<P.key:
            P.left=N
        elif k>P.key:
            P.right=N
        N.parent=P

def delete(N):
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
            X=next(N)     # X has no left child
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

def rotate_right(X):
    P=X.parent
    L=X.left
    X.left=L.right
    L.right.parent=X
    L.right=X
    L.parent=P
    X.parent=L
    if P.right.key==X.key:
        P.right=L
    else:
        P.left=L

def avl_insert(k,R):
    insert(k,R)
    N=find(k,R)
    rebalance(N)

def rebalance(N):
    P=N.parent
    if N.left.height>N.right.height+1:
        rebalance_right(N)
    elif N.right.height>N.left.height+1:
        rebalance_left(N)
    adjust_height(N)
    if P:
        rebalance(P)

def adjust_height(N):
    N.height=1+max(N.left.height,N.right.height)

def rebalance_right(N):
    M=N.left
    if M.right.height>M.left.height:
        rotate_left(M)
    rotate_right(N)
    adjust_height(N.right)
    adjust_height(N)
    adjust_height(M)
    adjust_height(M.parent)