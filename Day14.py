e='37'
i1,i2=0,1
useNum='286051'
#useNum=286051
while useNum not in e[-7:]:
    new_score=str(int(e[i1])+int(e[i2]))
    e+=new_score
    i1=(i1+int(e[i1])+1)%len(e)
    i2=(i2+int(e[i2])+1)%len(e)
print(e.index(useNum))
#for i in range(300000):
#    new_score=str(e[i1]+e[i2])
#    for x in new_score:
#        e.append(int(x))
#    i1=(i1+e[i1]+1)%len(e)
#    i2=(i2+e[i2]+1)%len(e)
#x=''
#for i in range(useNum,useNum+10):
#    x+=str(e[i])
#print(str(x))