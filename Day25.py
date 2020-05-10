from collections import deque
f=open('input.txt','r')
next=f.readline()
stars=[]
def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])+abs(a[3]-b[3])
while len(next)>0:
    s=next.split(',')
    stars.append((int(s[0]),int(s[1]),int(s[2]),int(s[3])))
    next=f.readline()
chained=set()
chains=[]
count=0
for i in range(len(stars)):
    if stars[i] not in chained:
        queue=deque()
        queue.append(stars[i])
        curChain=[]
        curChainSet=set()
        while queue:
            x=queue.popleft()
            if x not in curChainSet:
                curChainSet.add(x)
                curChain.append(x)
                chained.add(x)
                for j in range(len(stars)):
                    if dist(stars[j],x)<=3:
                        queue.append(stars[j])
        chains.append(curChain)
        count+=1
print(count)