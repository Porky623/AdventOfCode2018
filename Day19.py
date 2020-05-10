f=open('input.txt','r')
ipReg=4
ipVal=0
#Commands 9,10,11,3,4,5,6,8
#ipVal=8
registers=[0,0,0,0,0,0]
#registers=[10551349,0,10551347,10551348,7,10551347]
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
instructions=['addr','addi','mulr','muli','banr','bani','borr','bori','setr','seti','gtir','gtri','gtrr','eqir','eqri','eqrr']
inst=[]
for i in range(36):
    inst.append(f.readline().strip().split(' '))
count=0
while 0<=ipVal<len(inst):
    registers[ipReg]=ipVal
    curInst=inst[ipVal]
    operate(instructions.index(curInst[0]),int(curInst[1]),int(curInst[2]),int(curInst[3]),0)
    ipVal=registers[ipReg]
    ipVal+=1
    if(curInst[3]=='0'):
        print(registers, ipVal)
    #shows it increases every time a factor of registers[3] is reached in registers[2]:
    #sum of factors of registers[3]=10551348=2^2*3^2*293093=>7*13*293094=26671554
    count+=1
print(registers[0])