from collections import deque
dirMap={'N':0,'W':1,'E':2,'S':3}
changeMap={0:-1j, 1:-1,2:1,3:1j}
f=open('input.txt','r')
s=f.readline().strip()[1:-1]
map={0:[None,None,None,None]}
def getRParen(s):
    stack=[]
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(i)
        elif s[i]==')':
            if len(stack)==1:
                return i
            stack.pop()
def splitByPipe(s):
    stack=[]
    lastSeen=-1
    ret=[]
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(i)
        elif s[i]==')':
            stack.pop()
        elif s[i]=='|' and len(stack)==0:
            ret.append(s[lastSeen+1:i])
            lastSeen=i
    ret.append(s[lastSeen+1:])
    return ret
def makeNewMap(s,cur):
    global map
    if len(s)==0:
        return
    splits=splitByPipe(s)
    for s in splits:
        origCur=cur
        indOfLParen=s.find('(')
        indOfPipe=s.find('|')
        if indOfLParen>=0:
            while indOfPipe<indOfLParen:
                curString=s[:indOfPipe]
                for i in curString:
                    x=dirMap[i]
                    newNode=cur+changeMap[x]
                    if newNode not in map:
                        map[newNode]=[None,None,None,None]
                    map[newNode][3-dirMap[i]]=cur
                    map[cur][dirMap[i]]=newNode
                    cur=newNode
                cur=origCur
                s=s[indOfPipe+1:]
                indOfLParen=s.find('(')
                indOfPipe=s.find('|')
        while len(s)>0 and s[0]!='(':
            x=dirMap[s[0]]
            newNode=cur+changeMap[x]
            if newNode not in map:
                map[newNode]=[None,None,None,None]
            map[newNode][3-x]=cur
            map[cur][x]=newNode
            cur=newNode
            s=s[1:]
        if len(s)==0:
            cur=origCur
            continue
        indOfRParen=getRParen(s)
        if s[indOfRParen-1]=='|':
            makeNewMap(s[1:indOfRParen-1]+s[indOfRParen+1:],cur)
#            makeNewMap(s[indOfRParen+1:],cur)
        else:
            makeNewMap(s[1:indOfRParen],cur)
#        makeNewMap(s[indOfRParen+1:],cur)
        cur=origCur
#def makeMap(s,cur):
#    global map
#    if len(s)==0:
#        return
#    origCur=cur
#    indOfLParen=s.find('(')
#    indOfPipe=s.find('|')
#    if indOfLParen>=0:
#        while indOfPipe<indOfLParen:
#            curString=s[:indOfPipe]
#            for i in curString:
#                x=dirMap[i]
#                newNode=cur+changeMap[x]
#                if newNode not in map:
#                    map[newNode]=[None,None,None,None]
#                map[newNode][3-dirMap[i]]=cur
#                map[cur][dirMap[i]]=newNode
#                cur=newNode
#            cur=origCur
#            s=s[indOfPipe+1:]
#            indOfLParen=s.find('(')
#            indOfPipe=s.find('|')
#    while len(s)>0 and s[0]!='(':
#        if s[0]=='|':
#            cur=origCur
#            s=s[1:]
#        if len(s)==0:
#            break
#        x=dirMap[s[0]]
#        newNode=cur+changeMap[x]
#        if newNode not in map:
#            map[newNode]=[None,None,None,None]
#        map[newNode][3-x]=cur
#        map[cur][x]=newNode
#        cur=newNode
#        s=s[1:]
#    if len(s)==0:
#        return
#    indOfRParen=getRParen(s)
#    makeMap(s[1:indOfRParen],cur)
#    if s[indOfRParen-1]=='|':
#        makeMap(s[1:indOfRParen-1]+s[indOfRParen+1:],cur)
#    makeMap(s[indOfRParen+1:],cur)
#BFS
def findFarthestPath(cur,seen):
    queue=deque()
    seen[None]=0
    queue.append((cur,None))
    global map
    ind=[]
    curMax=0
    curCount=0
    while queue:
        cur,prev=queue.popleft()
        if cur in seen:
            continue
        adj=map[cur]
        seen[cur]=seen[prev]+1
        curMax=max(curMax,seen[cur])
        if seen[cur]>=1001:
            curCount+=1
        for i in range(4):
            if adj[i]!=None:
                ind.append(i)
        if len(ind)==0:
            continue
        for i in range(len(ind)):
            if adj[ind[i]] not in seen:
                queue.append((adj[ind[i]],cur))
    return curMax,curCount
makeNewMap(s,0+0j)
print(findFarthestPath(0,{}))