f=open('input.txt','r')
forest=[]
adj=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def getVal(x):
    row,col=x
    if 0<=row<len(forest) and 0<=col<len(forest[0]):
        return forest[row][col]
    return None
def add(a,b):
    return (a[0]+b[0],a[1]+b[1])
def calc(x):
    row,col=x
    curCount=[0,0,0]
    for a in adj:
        y=getVal(add(a,x))
        if y!=None:
            curCount[y]+=1
    val=getVal(x)
    if val==0:
        if curCount[1]>2:
            return 1
        return 0
    if val==1:
        if curCount[2]>2:
            return 2
        return 1
    if curCount[2]>0 and curCount[1]>0:
        return 2
    return 0
def resourceVal(minute):
    curCount=[0,0,0]
    for x in range(50):
        for y in range(50):
            curCount[forest[x][y]]+=1
    print('%d %d'%(curCount[1]*curCount[2],minute))
for i in range(50):
    forest.append([0 if x=='.' else 1 if x=='|' else 2 for x in f.readline().strip()])
#minutes=10
minutes=1000000000
for minute in range(minutes):
    newForest=[]
    for row in range(50):
        newForest.append([calc((row,col)) for col in range(50)])
    forest=newForest
    if minute%100==99:
        resourceVal(minute+1)
#resourceVal()
#Cycle by 700 starting at year 700: 
#10000000%7==3, so same as 1000