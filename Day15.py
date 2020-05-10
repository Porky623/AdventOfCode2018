import heapq
from collections import deque
adj=[(-1,0),(0,-1),(0,1),(1,0)]
def add(a,b):
    return (a[0]+b[0],a[1]+b[1])
def findInRange(seen,board,person,pos):
    queue=deque()
    queue.append((person[:2],[]))
    seen[person[:2]]=0
    while queue:
        nextPos=queue.pop()
        if nextPos[0] in seen:
            continue
        if board[nextPos[0][0]][nextPos[0][1]]<0:
            continue
        if nextPos[0] in pos and pos[nextPos[0]][3]==3-pos[person[:2]][3]:
            return [nextPos[1][0]]
        for a in adj:
            x=add(nextPos[0],a)
            queue.append((x,nextPos[1]+[x]))
        seen[nextPos[0]]=0
    return []
def move(board,person,pC,pos):
    moves=findInRange({},board,person,pos)
    for move in moves:
        person=(move[0],move[1],person[2],person[3])
def addGob(pC,pp,i,j,pos):
    x=(i,j,200,2)
    heapq.heappush(people,x)
    pC[2]+=1
    pos[(i,j)]=x
    return 0
def addElf(pC,pp,i,j,pos):
    x=(i,j,200,1)
    heapq.heappush(people,x)
    pC[1]+=1
    pos[(i,j)]=x
    return 0
def inRange(person,pos):
    for a in adj:
        if add(person[:2],a) in pos:
            return True
    return False
def attack(board,person,pC,pos,deleted):
    nextTo=[]
    for a in adj:
        checkedPos=add(person[:2],a)
        if checkedPos in pos and pos[checkedPos][3]==3-person[3]:
            nextTo.append(checkedPos)
    fewest=0
    for i in range(1,len(nextTo)):
        if pos[nextTo[i]][2]<pos[nextTo[fewest]][2]:
            fewest=i
    pos[nextTo[fewest]]=(pos[nextTo[fewest]][0],pos[nextTo[fewest]][1],pos[nextTo[fewest]][2]-3,pos[nextTo[fewest]][3])
    if pos[nextTo[fewest]][2]<=0:
        peopleCount[pos[nextTo[fewest]][3]]-=1;
        deleted[pos[nextTo[fewest]]]
        del pos[nextTo[fewest]]
f=open('input.txt','r')
board=[]
peopleCount=[0,0,0]
people=[]
pos={}
for i in range(32):
    s=f.readline().strip()
    board.append([-1 if x=='#' else 0 if x=='.' else addGob(peopleCount,people,i,j,pos) if x=='G' else addElf(peopleCount,people,i,j,pos) for j,x in enumerate(s)])
round=0
cont=True
while cont:
    newPeople=[]
    deleted={}
    while len(people)>0:
        person=heapq.heappop(people)
        if person in deleted:
            continue
        if peopleCount[3-person[3]]==0:
            cont=False
        elif inRange(person,pos):
            attack(board,person,peopleCount,pos,deleted)
        else:
            person=move(board,person,peopleCount,pos)
            attack(board,person,peopleCount,pos,deleted)
        heapq.heappush(newPeople,person)
    people=newPeople
    round+=1
sumHit=0
for person in people:
    sumHit+=person[2]
print(round*sumHit)