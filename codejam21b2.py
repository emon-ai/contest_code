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
        #t=list(s)
        t=s
        #j=list(j)
        for k in range(m):
            t=t.replace("?",j[k],1)
            #j.remove(j[0])
            """if t[k]=="?":
                t[k]=j[0]
                j.remove(j[0])"""
        #print(t)
        if l>(t.count("CJ")*int(x)+t.count("JC")*int(y)):
            l=t.count("CJ")*int(x)+t.count("JC")*int(y)
    print("Case #%d:"%(i+1),l)