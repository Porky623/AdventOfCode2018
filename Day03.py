f=open("input.txt",'r')
inputs=f.readlines()
sections=[]
ind=0
for s in inputs:
    s=s.strip().split(' ')
    sp=(s[2].split(','),s[3].split('x'))
    sections.append((int(s[0][1:]),int(sp[0][0]),int(sp[0][1][:len(sp[0][1])-1]),int(sp[1][0]),int(sp[1][1])))
    ind+=1
for k in range(1349):
    map={}  
    for i in range(sections[k][3]):
        for j in range(sections[k][4]):
            map[sections[k][1]+i,sections[k][2]+j]=1
    work=True
    for ind in range(1349):
        if ind!=k:
            for i in range(sections[ind][3]):
                for j in range(sections[ind][4]):
                    x=sections[ind][1]+i,sections[ind][2]+j
                    if x in map:
                        work=False
    if work:
        print(k+1)