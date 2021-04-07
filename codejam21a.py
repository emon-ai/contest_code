for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split(" ")))
    s=0
    for j in range(0,n-1):
        k=l.index(min(l[j:n]))
        l[j:k+1]=reversed(l[j:k+1])
        s+=(k-j+1)
    print("Case #%d:"%(i+1),s)