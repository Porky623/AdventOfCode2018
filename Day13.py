import sys
def getDir(dir):
    chars=['^','>','v','<']
    return chars.index(dir)
def addCart(carts,character,col,row,positions):
    positions[(row,col)]=0
    cart=(row,col,getDir(character),0)
    carts.append(cart)
    return 1 if cart[2]%2==0 else 2
def add(a, b):
    return (a[0]+b[0],a[1]+b[1])
f=open("input.txt",'r')
st=f.readline()
tracks=[]
carts=[]
ind=0
positions={}
while len(st)>0 and st!='\n':
    tracks.append([0 if x==' ' else -1 if x=='+' else 1 if x=='|' else 2 if x=='-' else 3 if x=='/' else 4 if x=='\\' else addCart(carts,x,i,ind,positions) for i,x in enumerate(st[:-1])])
    st=f.readline()
    ind+=1
carts.sort()
#0 is up, 1 is right, 2 is down, 3 is left
changes=((-1,0),(0,1),(1,0),(0,-1))
up,right,down,left=0,1,2,3
numCarts=17
while numCarts>1:
    carts.sort()
    for i,cart in enumerate(carts):
        if cart==(0,0,0,0):
            continue
        del positions[cart[:2]]
        newPos=cart[:2]
        if tracks[cart[0]][cart[1]]==-1:
            dir=cart[2]
            if cart[3]==0:
                newPos=add(newPos,changes[(cart[2]+3)%4])
                dir=(dir+3)%4
            elif cart[3]==1:
                newPos=add(newPos,changes[cart[2]])
            else:
                newPos=add(newPos,changes[(cart[2]+1)%4])
                dir=(dir+1)%4
            newVal=(cart[3]+1)%3
            cart=(newPos[0],newPos[1],dir,newVal)
        elif tracks[cart[0]][cart[1]]==0:
            print('off the track!')
        elif tracks[cart[0]][cart[1]]<3:
            newPos=add(cart[:2],changes[cart[2]])
            cart=(newPos[0],newPos[1],cart[2],cart[3])
        elif tracks[cart[0]][cart[1]]==3:
            if cart[2]==up or cart[2]==down:
                newPos=add(cart[:2],changes[cart[2]+1])
                cart=(newPos[0],newPos[1],cart[2]+1,cart[3])
            else:
                newPos=add(cart[:2],changes[cart[2]-1])
                cart=(newPos[0],newPos[1],cart[2]-1,cart[3])
        else:
            if cart[2]==down or cart[2]==up:
                newPos=add(cart[:2],changes[(cart[2]-1)%4])
                cart=(newPos[0],newPos[1],(cart[2]-1)%4,cart[3])
            else:
                newPos=add(cart[:2],changes[(cart[2]+1)%4])
                cart=(newPos[0],newPos[1],(cart[2]+1)%4,cart[3])
        if cart[:2] in positions:
#            print('%d %d'%(cart[1],cart[0]))
#            sys.exit(0)
            carts[i]=(0,0,0,0)
            for j in range(len(carts)):
                if carts[j]==(0,0,0,0):
                    continue
                if carts[j][:2]==cart[:2]:
                    carts[j]=(0,0,0,0)
                    break
            del positions[cart[:2]]
            numCarts-=2
        else:
            positions[cart[:2]]=i
            carts[i]=cart
for i in range(17):
    if carts[i]!=(0,0,0,0):
        print('%d %d'%(carts[i][1],carts[i][0]))