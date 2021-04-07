for i in range(int(input())):
    x,y,s=map(str,input().split(" "))
    a=""
    x1,y1=0,0
    l=0
    for k in range(len(s)):
        if s[k]=="C":
            if a=="J":                   
                y1+=1
            a="C"
        elif s[k]=="J":
            if a=="C":                   
                x1+=1
            a="J"
    print("Case #%d:"%(i+1),(int(x)*x1+int(y)*y1))