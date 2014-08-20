from scipy.cluster.hierarchy import fcluster, linkage, dendrogram
from scipy import spatial
import matplotlib.pyplot as plt
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
    fp=open(r'F:\download\chapter\chapter\blogdata.txt', 'r')
    try:
        for line in fp:
            temp=line.split('\t')
            name.append(temp[0])
            matData.append(temp[1:])
    finally:
        fp.close()
    #print name
    distance = spatial.distance.pdist(matData)
    linkresult=linkage(distance, 'single', 'euclidean')
    Llink=len(linkresult)+1
    
    for index, item in enumerate(reversed(linkresult)):
        print item, index
        nodes[2*Llink-2-index]=node(int(item[0]), int(item[1]))
    for index in xrange(99):
        nodes[index]=node(-1, -1)
    
    que=[]
    s=''
    que.append(2*Llink-2)
    fp=open('linkage.txt', 'w')
    try:
        while len(que)!=0:
            temp=que.pop(0)
            if temp!=-1:
                fp.write(str(temp))
                que.append(nodes[temp].left)
                que.append(nodes[temp].right)
            else:
                fp.write(str(temp))
    finally:
        fp.close()
    print '1'
#    f=open('linkage.txt', 'w')
#    try:
#    fc=fcluster(linkresult,t=0.9,criterion='inconsistent',depth=2,R=None,monocrit=None)
#    print fc
#    f=open('fluster.txt', 'w')
#    try:
#        for num, item in enumerate(fc):
#            pass
#    finally:
#        f.close()
    #dendrogram(linkresult,get_leaves=False,show_leaf_counts=False)

if __name__=='__main__':
    func()
