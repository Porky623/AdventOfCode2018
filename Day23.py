f=open('input.txt','r')
next=f.readline()
bots=[]
#max=0
def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])
def add(a,b):
    return a[0]+b[0],a[1]+b[1],a[2]+b[2]
pos={}
dirs=[(-1,-1,-1),(-1,-1,1),(-1,1,-1),(-1,1,1),(1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1)]
def mult(a,b):
    return (a[0]*b[0],a[1]*b[1],a[2]*b[2])
optimal=(0,0)
distances={}
while len(next)>0:
    input=next[5:].strip().split('>, r=')
    input1=input[0].strip().split(',')
    bots.append((int(input1[0]),int(input1[1]),int(input1[2]),int(input[1])))
#    if bots[-1][3]>bots[max][3]:
#        max=len(bots)-1
    done=set()
    for i in range(bots[-1][3]):
        for j in range(bots[-1][3]-i):
            for k in range(bots[-1][3]-i-j):
                for dir in dirs:
                    newPos=add(mult((i,j,k),dir),bots[-1][:3])
                    if newPos in done:
                        break
                    done.add(newPos)
                    if newPos in pos:
                        pos[newPos]+=1
                    else:
                        pos[newPos]=1
                    if newPos not in distances:
                        distances[newPos]=dist(newPos,(0,0,0))
                    curDist=distances[newPos]
                    if pos[newPos]>optimal[1] or pos[newPos]==optimal[1] and curDist<optimal[0]:
                        optimal=curDist,pos[newPos]
    next=f.readline()
print(optimal[0])