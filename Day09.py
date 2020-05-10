from collections import deque
numPlayers=419;
lastMarble=7105200;
players=[0]*numPlayers
marbles=deque()
marbles.append(0)
curInd=0
for addedMarble in range(1,lastMarble+1):
    if addedMarble%23==0:
        marbles.rotate(7)
        players[(addedMarble-1)%numPlayers]+=addedMarble+marbles.pop()
        marbles.rotate(-1)
    else:
        marbles.rotate(-1)
        marbles.append(addedMarble)
max=players[0];
for i in range(numPlayers):
    if max<players[i]:
        max=players[i]
print(max)