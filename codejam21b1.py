def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
for i in range(int(input())):
    x,y,s=map(str,input().split(" "))
    m=s.count("?")
    l=1000000000000000000000
    for j in product("CJ",repeat=m):
        t=list(s)
        #t=s
        #j=list(j)
        z=0
        for k in range(len(t)):            
            if t[k]=="?":          
                t[k]=j[z]
                z+=1
        x1,y1="".join(map(str,t)).count("CJ"),"".join(map(str,t)).count("JC")
        if l>(x1*int(x)+y1*int(y)):
            l=(x1*int(x)+y1*int(y))
    print("Case #%d:"%(i+1),l)