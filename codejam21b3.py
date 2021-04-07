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
    l=[]
    for j in product("CJ",repeat=m):
        #t=list(s)
        t=s
        for k in range(m):
            t=t.replace("?",list(j[0]),1)
            list(j).remove(list(j)[0])
            """if t[k]=="?":
                t[k]=j[0]
                j.remove(j[0])"""
        #print(t)
        l.append(t.count("CJ")*int(x)+t.count("JC")*int(y))
    print("Case #%d:"%(i+1),min(l))