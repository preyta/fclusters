from scipy.cluster.hierarchy import fcluster, linkage, dendrogram
from scipy import spatial
import numpy as np

class node:
    def __init__(self, left, right):
        self.left=left
        self.right=right

def func():
    matData=[]
    name=[]
    nodes={}
    #fp=open(r'E:\nstl\fcluster\data\data3.txt', 'r')
    fp=open(r'blogdata.txt', 'r')
    try:
        for line in fp:
            temp=line.split('\t')
            name.append(temp[0])
            matData.append(temp[1:])
    finally:
        fp.close()
    #print name
    distance = spatial.distance.pdist(matData)
    linkresult=linkage(distance, 'average', 'euclidean')
    Llink=len(linkresult)+1
    
    for index, item in enumerate(reversed(linkresult)):
        print item, index
        nodes[2*Llink-2-index]=node(int(item[0]), int(item[1]))
    for index in xrange(99):
        nodes[index]=node(-1, -1)
    
    que=[]
    que.append(2*Llink-2)
    fp=open('linkage.txt', 'w')
    fp.write(str(2*Llink-2))
    fp.write('\n')
    future=0
    current=1
    try:
        while len(que)!=0:
            if current==0:
                current=future
                future=0
                fp.write('\n')
            temp=que.pop(0)
            current=current-1
            if temp<=98:
                fp.write(' || ')
            else:
               if nodes[temp].left==-1:
                   future=future+1
                   if nodes[temp].left<=98:
                       fp.write(name[nodes[temp].right])
                   else:
                       fp.write(str(nodes[temp].right))
                   fp.write(' || ')
               elif nodes[temp].right==-1:
                   future=future+1
                   if nodes[temp].left<=98:
                       fp.write(name[nodes[temp].left])
                   else:
                       fp.write(str(nodes[temp].left))
                   fp.write(' || ')
               else:
                   future=future+2
                   if nodes[temp].left<=98:
                       fp.write(name[nodes[temp].left])
                   else:
                       fp.write(str(nodes[temp].left))
                   fp.write('  ')
                   if nodes[temp].right<=98:
                       fp.write(name[nodes[temp].right])
                   else:
                       fp.write(str(nodes[temp].right))
                   fp.write(' || ')
               que.append(nodes[temp].left)
               que.append(nodes[temp].right)
    finally:
        fp.close()
    print '1'
#    f=open('linkage.txt', 'w')
#    try:
    fc=fcluster(linkresult,t=0.8,criterion='inconsistent',depth=2,R=None,monocrit=None)
    print fc
#    f=open('fluster.txt', 'w')
#    try:
#        for num, item in enumerate(fc):
#            pass
#    finally:
#        f.close()
    #dendrogram(linkresult,get_leaves=False,show_leaf_counts=False)

if __name__=='__main__':
    func()
