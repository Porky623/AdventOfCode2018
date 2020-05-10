def show(pos):
    f=open("output.txt",'w')
    minX,minY,maxX,maxY=min(x[0] for x in pos),min(x[1] for x in pos),max(x[0] for x in pos),max(x[1] for x in pos)
    dict={}
    for i in range(len(pos)):
        dict[pos[i][0],pos[i][1]]=True
    for j in range(minX,maxX+1):
        s=''
        for i in range(minY,maxY+1):
            if (j,i) in dict:
                s+='#'
            else:
                s+='.'
        f.print(s)
f=open("input.txt",'r')
next=f.readline()
pos=[]
vel=[]
while next!=None:
    input=next.split('<')
    inp=input[1].split(', ')
    pos.append((int(inp[0].strip()[:-1]),int(inp[1].strip().split('> ')[0])))
    inp=input[2].split(', ')
    vel.append((int(inp[0].strip()),int(inp[1].strip()[:-1])))
    next=f.readline()
for i in range(10):
    show(pos)
    for i in range(len(pos)):
        pos[i]+=vel[i]
