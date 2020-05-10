class Unit:
    def __init__(self,ind,num,hp,imm,weak,init,dmgType,dmg,army):
        self.ind=ind
        self.num=num
        self.hp=hp
        self.scales=[1 for i in range(5)]
        for i in range(5):
            if i in imm:
                self.scales[i]=0
            elif i in weak:
                self.scales[i]=2
        self.init=init
        self.dT=dmgType
        self.dmg=dmg
        self.army=army
    def eP(self):
        return self.num*self.dmg
    def dmging(self,targ):
        return targ.scales[self.dT]*self.eP()
units=[]
types=['bludgeoning','cold','fire','radiation','slashing']
for line in open('input.txt').read().strip().split('\n'):
    if 'Immune System' in line:
        ind=1
        army=0
    elif 'Infection' in line:
        ind=1
        army=1
    elif line:
        words=line.split(' ')
        num=int(words[0])
        hp=int(words[4])
        imm,weak=set(),set()
        if '(' in line:
            check=line.split('(')[1].split(')')[0]
            halves=check.split('; ')
            for s in halves:
                if not s:
                    continue
                for i in range(5):
                    if types[i] in s:
                        (imm if 'immune' in s else weak).add(i)
        init=int(words[-1])
        dmgType=int(types.index(words[-5]))
        dmg=int(words[-6])
        units.append(Unit('{}_{}'.format({1:'Infection',0:'System'}[army],ind),num,hp,imm,weak,init,dmgType,dmg,army))
        ind+=1
def battle(orig_units,boost):
    units=[]
    for u in orig_units:
        units.append(Unit(u.ind,u.num,u.hp,{i for i in range(5) if u.scales[i]==0},{i for i in range(5) if u.scales[i]==2},u.init,u.dT,u.dmg+(boost if u.army==0 else 0),u.army))
    while True:
        units=sorted(units,key=lambda u:(-u.eP(),-u.init))
        chosen=set()
        for u in units:
            def tKey(targ):
                return (-u.dmging(targ),-targ.eP(),-targ.init)
            targets=sorted([targ for targ in units if targ.army!=u.army and targ.ind not in chosen and u.dmging(targ)>0],key=tKey)
            while targets and targets[0].ind in chosen:
                targets=targets[1:]
            if targets:
                u.target=targets[0]
                chosen.add(targets[0].ind)
        units=sorted(units,key=lambda u:-u.init)
        someDead=False
        for u in units:
            if u.target:
                dmg=u.dmging(u.target)
                killed=min(u.target.num,int(dmg/u.target.hp))
                if killed>0:
                    someDead=True
                u.target.num-=killed
        units=[u for u in units if u.num>0]
        for u in units:
            u.target=None
        n0=sum([u.num for u in units if u.army==0])
        n1=sum([u.num for u in units if u.army==1])
        if not someDead:
            return 1,0
        if n0==0:
            return 1,n1
        elif n1==0:
            return 0,n0
print(battle(units,0))
boost=0
while True:
    winner,left=battle(units,boost)
    if winner==0:
        print(left)
        break
    boost+=1