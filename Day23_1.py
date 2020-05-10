from pulp import *
from itertools import product
f=open('input.txt','r')
next=f.readline()
bots=[]
def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])
maxInd=0
while len(next)>0:
    input=next[5:].strip().split('>, r=')
    input1=input[0].strip().split(',')
    bots.append((int(input1[0]),int(input1[1]),int(input1[2]),int(input[1])))
    if bots[-1][3]>bots[maxInd][3]:
        maxInd=len(bots)-1
    next=f.readline()
prob=LpProblem("problem",LpMaximize)
cat='Integer'
#cat='Continuous'
counts=[LpVariable("c_{}".format(i),lowBound=0,upBound=1,cat='Integer')for i in range(len(bots))]
x,y,z=LpVariable('x'),LpVariable('y'),LpVariable('z')
totalCount=LpVariable('totalCount')
prob+=totalCount
prob+=totalCount==sum(counts)
for i,(x_i,y_i,z_i,r_i) in enumerate(bots):
    c_i=counts[i]
    for sign in product([-1,1],repeat=3):
        prob+=(
                sign[0]*(x-x_i)+
                sign[1]*(y-y_i)+
                sign[2]*(z-z_i))<=r_i+(1-c_i)*int(1e10)
status=prob.solve()
print('x,y,z',value(x),value(y),value(z))
print('sum',value(x)+value(y)+value(z))