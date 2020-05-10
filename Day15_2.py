from collections import deque
import copy
import math
att=[0,3,3]
def add(a,b):
    return (a[0]+b[0],a[1]+b[1])
def addGob(i,j,pos,pC):
    pos[(i,j)]=(200,2)
    pC[2]+=1
    return 0
def addElf(i,j,pos,pC):
    pos[(i,j)]=(200,1)
    pC[1]+=1
    return 0
def findNextMove(startPos,pos,board):
    queue=deque()
    queue.append((startPos,[startPos]))
    seen={}
    while queue:
        nextPos=queue.popleft()
        if nextPos[0] in seen:
            continue
        if board[nextPos[0][0]][nextPos[0][1]]<0 or pos[nextPos[0]][1]==pos[startPos][1] and nextPos[0]!=startPos:
            continue
        if pos[nextPos[0]][0]>0 and pos[nextPos[0]][1]==3-pos[startPos][1]:
            if len(nextPos[1])==2:
                return startPos
            if len(nextPos[1])>1:
                pos[nextPos[1][1]]=(pos[startPos])
                pos[startPos]=(-1,-1)
                return nextPos[1][1]
            return nextPos[1][0]
        for a in adj:
            x=add(nextPos[0],a)
            queue.append((x,nextPos[1]+[x]))
        seen[nextPos[0]]=0
    return None
def move(startPos,pos,board):
    pos=findNextMove(startPos,pos,board)
    return startPos if pos==None else pos
def attack(startPos,pos,board,pC):
    work=[]
    for i,a in enumerate(adj):
        x=add(startPos,a)
        if pos[x][0]>0 and pos[x][1]==3-pos[startPos][1]:
            work.append(x)
    if len(work)==0:
        return
    minHp=0
    for i in range(1,len(work)):
        if pos[work[minHp]][0]>pos[work[i]][0]:
            minHp=i
    x=work[minHp]
    if pos[x][0]<att[pos[startPos][1]]+1:
        pC[pos[x][1]]-=1
        pos[x]=(-1,-1)
        return
    pos[x]=(pos[x][0]-att[pos[startPos][1]],pos[x][1])
    return
numLine=32
numCol=32
f=open('input.txt','r')
board=[]
pos={}
adj=[(-1,0),(0,-1),(0,1),(1,0)]
for i in range(numLine):
    for j in range(numCol):
        pos[(i,j)]=(-1,-1)
personCount0=[0,0,0]
for i in range(numLine):
    s=f.readline().strip()
    temp=[]
    for j in range(len(s)):
        if s[j]=='#':
            temp.append(-1)
        elif s[j]=='.':
            temp.append(0)
        elif s[j]=='G':
            temp.append(addGob(i,j,pos,personCount0))
        else:
            temp.append(addElf(i,j,pos,personCount0))
    board.append(temp)
#    board.append([-1 if x=='#' else 0 if x=='.' else addGob(i,j,pos,personCount) if x=='G' else addElf(i,j,pos,personCount) for j,x in enumerate(s)])
round=0
elfLose=True
adjPos=0
while elfLose:
    cont=True
    round=0
    adjPos=copy.deepcopy(pos)
    personCount=copy.copy(personCount0)
    while cont:
        toMove=deque()
        for i in range(1,numLine):
            for j in range(1,numCol):
                if adjPos[(i,j)][0]>0:
                    toMove.append((i,j))
        toMoveLength=len(toMove)
        if personCount[1]==0 or personCount[2]==0:
            cont=False
            continue
        for x in range(toMoveLength):
            if not cont:
                continue
            personPos=toMove.popleft()
            if adjPos[personPos][0]<0:
                continue
            person=move(personPos,adjPos,board)
            if personCount[3-adjPos[person][1]]==0:
                cont=False
            attack(person,adjPos,board,personCount)
        if cont:
            round+=1
    if personCount[1]==10:
        elfLose=False
    att[1]+=1
sum=0
for i in range(1,numLine):
    for j in range(1,numCol):
        if adjPos[(i,j)][0]>0:
            sum+=adjPos[(i,j)][0]
print(sum*round)