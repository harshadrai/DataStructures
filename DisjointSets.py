class DisjointSets(object):
    def __init__(self):
        self.parent={}
        self.rank={}
    def make_set(self,i):
        self.parent[i]=i
        self.rank[i]=0
    def find(self,i):
        if i != self.parent.get(i):
            self.parent[i]=self.find(self.parent.get(i))
        return self.parent.get(i)
    def union(self,i,j):
        i_id=self.find(i)
        j_id=self.find(j)
        if i_id==j_id:
            return
        else:
            if self.rank[i_id] > self.rank[j_id]:
                self.parent[j_id]=i_id
            else:
                self.parent[i_id]=j_id
                if self.rank[i_id]==self.rank[j_id]:
                    self.rank[j_id]+=1


my_disjoint_set=DisjointSets()
my_disjoint_set.make_set(1)
my_disjoint_set.make_set(2)
my_disjoint_set.make_set(3)
my_disjoint_set.union(1,2)
my_disjoint_set.union(1,3)
my_disjoint_set.find(3)
my_disjoint_set.find(my_disjoint_set.find(3))==my_disjoint_set.find(3)
my_disjoint_set.find(1)
my_disjoint_set.make_set(4)
my_disjoint_set.make_set(5)
my_disjoint_set.make_set(7)
my_disjoint_set.union(4,7)
my_disjoint_set.union(4,5)
my_disjoint_set.find(4)
my_disjoint_set.find(5)
my_disjoint_set.union(4,1)
my_disjoint_set.rank[4]
my_disjoint_set.rank[2]
my_disjoint_set.rank[7]
my_disjoint_set.parent[4]
my_disjoint_set.find(4)
my_disjoint_set.parent[4]
my_disjoint_set.parent[5]
my_disjoint_set.find(5)
my_disjoint_set.parent[5]
my_disjoint_set.parent[7]
my_disjoint_set.find(7)
my_disjoint_set.find(6)
