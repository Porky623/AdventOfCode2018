#bludg, cold, fire, rad,slash
#numUnit, hitpt, immunities (x5), dmg, dmg type, init
import heapq
immune=[(2749,8712,1,0,2,0,1,30,3,18),(704,1890,1,1,1,1,1,26,2,17),(1466,7198,0,2,1,1,2,44,0,6)
,(6779,11207,1,1,1,1,1,13,1,4),(1275,11747,1,1,1,1,1,66,1,2),(947,5442,1,1,1,1,1,49,3,3),(4319,2144,2,1,2,1,1,4,2,9)
,(6315,5705,1,1,1,1,1,7,1,16),(8790,10312,1,1,1,1,1,10,2,5),(3242,4188,1,2,1,0,1,11,0,14)]
infect=[(1230,11944,1,2,1,1,1,17,0,1),(7588,53223,0,1,1,1,1,13,1,12),(1887,40790,1,0,1,0,0,43,2,15)
,(285,8703,1,1,1,1,0,60,4,7),(1505,29297,1,1,1,1,1,38,2,8),(191,24260,0,1,1,1,2,173,1,20)
,(1854,12648,1,2,2,1,1,13,0,13),(1541,49751,2,2,1,1,1,62,4,19),(3270,22736,1,1,1,1,1,13,4,10),(1211,56258,1,0,1,1,0,73,0,11)]
#0: -1*effPow,1: -1*init,2: num,3: hipt,4-8: imm,9: dmg,10: dmgtype, 11: imm/inf, 12: index
for i in range(len(immune)):
    a=immune[i]
    immune[i]=(-1*a[0]*a[7],-1*a[9],a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],0,i)
for i in range(len(infect)):
    a=infect[i]
    infect[i]=(-1*a[0]*a[7],-1*a[9],a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],1,i)
while len(immune)>0 and len(infect)>0:
    attackPQ=[]
    chosen={}
    choosing={}
    #-1*init,type,index
    actualPQ=[]
    for a in immune:
        heapq.heappush(attackPQ,a)
    for a in infect:
        heapq.heappush(attackPQ,a)
    while attackPQ:
        a=heapq.heappop(attackPQ)
        if a[11]==0:
            curMax=-1,0
            for i in range(0,len(infect)):
                dmg=-1*a[0]*infect[i][4+a[10]]
                if dmg>curMax[1] and (i,1) not in chosen and infect[i][1]<infect[curMax[0]][1]:
                    curMax=i,dmg
            if curMax[0]<0:
                continue
            chosen[(curMax[0],1)]=a[10]
            choosing[(0,a[12])]=curMax[0],curMax[1]
            heapq.heappush(actualPQ,(a[1],0,a[12]))
        else:
            curMax=-1,0
            for i in range(0,len(immune)):
                dmg=-1*a[0]*immune[i][4+a[10]]
                if dmg>curMax[1] and (i,0) not in chosen and immune[i][1]<immune[curMax[0]][1]:
                    curMax=i,dmg
            if curMax[0]<0:
                continue
            chosen[(curMax[0],0)]=a
            choosing[(1,a[12])]=curMax[0],curMax[1]
            heapq.heappush(actualPQ,(a[1],1,a[12]))
    while actualPQ:
        init,typ,ind=heapq.heappop(actualPQ)
        #if isImmune
        if typ==0:
            if immune[ind][0]==0:
                continue
            target=choosing[(0,ind)]
            targ=infect[target[0]]
            if targ[2]<=int(target[1]/targ[3]):
                infect[target[0]]=0,targ[1],0,targ[3],targ[4],targ[5],targ[6],targ[7],targ[8],targ[9],targ[10],targ[11],targ[12]
            else:
                newNum=targ[2]-int(target[1]/targ[3])
                infect[target[0]]=-1*newNum*targ[9],targ[1],newNum,targ[3],targ[4],targ[5],targ[6],targ[7],targ[8],targ[9],targ[10],targ[11],targ[12]
        else:
            if infect[ind][0]==0:
                continue
            target=choosing[(1,ind)]
            targ=immune[target[0]]
            if targ[2]<=int(target[1]/targ[3]):
                immune[target[0]]=0,targ[1],0,targ[3],targ[4],targ[5],targ[6],targ[7],targ[8],targ[9],targ[10],targ[11],targ[12]
            else:
                newNum=targ[2]-int(target[1]/targ[3])
                immune[target[0]]=-1*newNum*targ[9],targ[1],newNum,targ[3],targ[4],targ[5],targ[6],targ[7],targ[8],targ[9],targ[10],targ[11],targ[12]
maxUn=0
if len(immune)>0:
    for i in range(len(immune)):
        maxUn+=immune[i][2]
else:
    for i in range(len(infect)):
        maxUn+=infect[i][2]
print(maxUn)