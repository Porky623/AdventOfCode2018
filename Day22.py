import sys
import heapq
def isValid(eV,t,g):
    if eV==0:
        return (t or g)
    if eV==1:
        return g or not t and not g
    return t or not t and not g
def add(a,b):
    return (a[0]+b[0],a[1]+b[1])
f=open('input.txt','r')
depth=4080
target=14,785
kx,ky=16807,48271
geoInd={(0,0):0,target:0}
#sum=0
erosion={}
for a in range(target[0]+100):
    for b in range(target[1]+100):
        if not((a,b)==(0,0) or (a,b)==target):
            if b==0:
                geoInd[(a,b)]=a*kx
            elif a==0:
                geoInd[(a,b)]=b*ky
            elif (a,b)!=target:
                geoInd[(a,b)]=(erosion[(a-1,b)]*erosion[(a,b-1)])%20183
        erosion[(a,b)]=(geoInd[(a,b)]+depth)%20183
#        sum+=erosion[(a,b)]%3
#print(sum)
pq=[]
seen={}
heapq.heappush(pq,(0,(0,0),True,False))
adj=[(-1,0),(1,0),(0,-1),(0,1)]
while pq:
    time,pos,torch,gear=heapq.heappop(pq)
    if (pos,torch,gear) in seen:
        continue
    seen[(pos,torch,gear)]=0
    val=erosion[pos]%3
    if not isValid(val,torch,gear):
        continue
    if (pos,torch)==(target,True):
        print(time)
        break
    for a in adj:
        newPos=add(pos,a)
        if newPos in erosion:
            heapq.heappush(pq,(time+1,newPos,torch,gear))
    time+=7
    if val==0:
        heapq.heappush(pq,(time,pos,True,False))
        heapq.heappush(pq,(time,pos,False,True))
    elif val==1:
        heapq.heappush(pq,(time,pos,False,True))
        heapq.heappush(pq,(time,pos,False,False))
    elif val==2:
        heapq.heappush(pq,(time,pos,True,False))
        heapq.heappush(pq,(time,pos,False,False))