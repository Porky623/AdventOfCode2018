from collections import defaultdict
f=open('input.txt','r')
grid,settled,flowing=defaultdict(bool),set(),set()
minX,minY,maxX,maxY=2000,2000,0,0
def floodFill(p,dir=1j):
    left,right,down=p-1,p+1,p+1j
    flowing.add(p)
    if not grid[down]:
        if down not in flowing and 1<=down.imag<=maxY:
            floodFill(p+1j)
        if down not in settled:
            return False
    endLeft=grid[left] or left not in flowing and floodFill(left,-1)
    endRight=grid[right] or right not in flowing and floodFill(right,1)
    if dir==1j and endLeft and endRight:
        settled.add(p)
        cur=left
        while cur in flowing:
            settled.add(cur)
            cur-=1
        cur=right
        while cur in flowing:
            settled.add(cur)
            cur+=1
    return dir==-1 and (endLeft or grid[left]) or dir==1 and (endRight or grid[right])
for i in range(1470):
    s=f.readline().strip().split(', ')
    s2=s[1].split('..')
    a1,a2,a3=int(s[0][2:]),int(s2[0][2:]),int(s2[1])
    if s[0][0]=='x':
        for a in range(a2,a3+1):
            grid[a1+a*1j]=True
        minX,minY,maxX,maxY=min(minX,a1),min(minY,a2),max(maxX,a1),max(maxY,a3)
    else:
        for a in range(a2,a3+1):
            grid[a+a1*1j]=True
        minX,minY,maxX,maxY=min(minX,a2),min(minY,a1),max(maxX,a3),max(maxY,a1)
floodFill(500)
Water=flowing
Water.update(settled)
print(len([water for water in Water if minY<=water.imag<=maxY]))
print(len([water for water in settled if minY<=water.imag<=maxY]))
#out=open('day17.csv','w')
#for a in range(minX,maxX+1):
#    for b in range(minY,maxY+1):
#        out.write('%d,'%grid[a][b])
#    out.write('\n')
#out.close()
#minX,maxX,minY,maxY=404,628,6,1631