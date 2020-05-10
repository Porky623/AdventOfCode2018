registers=[]
aftReg=[]
def operate(a,b,c,d,code):
    if code>0:
        if a==0:
            return registers[b]+registers[c]
        if a==1:
            return registers[b]+c
        if a==2:
            return registers[b]*registers[c]
        if a==3:
            return registers[b]*c
        if a==4:
            return registers[b]&registers[c]
        if a==5:
            return registers[b]&c
        if a==6:
            return registers[b]|registers[c]
        if a==7:
            return registers[b]|c
        if a==8:
            return registers[b]
        if a==9:
            return b
        if a==10:
            return int(b>registers[c])
        if a==11:
            return int(registers[b]>c)
        if a==12:
            return int(registers[b]>registers[c])
        if a==13:
            return int(b==registers[c])
        if a==14:
            return int(registers[b]==c)
        return int(registers[b]==registers[c])
    else:
        registers[d]=operate(a,b,c,d,1)
f=open('input.txt','r')
#count=0
canWork=[]
for i in range(16):
    canWork.append({})
for i in range(790):
    registers=[]
    aftReg=[]
    before=f.readline().strip().split(': ')
    for x in before[1][1:-1].split(', '):
        registers.append(int(x))
    inp=f.readline().split(' ')
    instruct=[]
    for x in inp:
        instruct.append(int(x))
    after=f.readline().strip().split(':  ')
    for x in after[1][1:-1].split(', '):
        aftReg.append(int(x))
    f.readline()
#    curCount=0
    for x in range(16):
        if aftReg[instruct[3]]==operate(x,instruct[1],instruct[2],instruct[3],1):
            canWork[instruct[0]][x]=0
#            curCount+=1
#    if curCount>=3:
#        count+=1
#print(count)
            
finalMap={}
for i in range(16):
    cont=True
    j=0
    while j<16 and cont:
        if len(canWork[j])==1:
            finalMap[j]=list(canWork[j].keys())[0]
            for x in range(16):
                if finalMap[j] in canWork[x]:
                    del canWork[x][finalMap[j]]
                    cont=False
        j+=1
registers=[0,0,0,0]
for i in range(927):
    s=f.readline().strip().split(' ')
    operate(finalMap[int(s[0])],int(s[1]),int(s[2]),int(s[3]),0)
print(registers[0])