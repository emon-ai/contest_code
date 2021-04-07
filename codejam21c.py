from itertools import permutations
def rsort(l):
    s=0
    n=len(l)
    for j in range(0,n-1):
        k=l.index(min(l[j:n]))
        l[j:k+1]=reversed(l[j:k+1])
        s+=(k-j+1)
    return s
for i in range(int(input())):
    x,y=map(int,input().split(" "))
    for j in permutations(range(1,x+1)):
        if rsort(list(j))==y:
            print("Case #%d:"%(i+1),' '.join(map(str,j)))
            break
    else:
        print("Case #%d:"%(i+1),"IMPOSSIBLE")