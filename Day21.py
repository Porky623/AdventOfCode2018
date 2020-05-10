import sys
r2,r3=0,0
lastSeen=None
seenSet=set()
seen=set()
r2=65536
r3=10736359
while True:
    r1=r2%256
    r3=(((r3+r1)%16777216)*65899)%16777216
    if r2<256:
        if r3 not in seenSet:
            lastSeen=r3
        seenSet.add(r3)
        r2=r3|65536
        if r2 in seen:
            print(lastSeen)
            sys.exit(0)
        seen.add(r2)
        r3=10736359
    else:
        r2=int(r2/256)