def strrev(s):
    if len(s)==1:
        return s
    p=""
    for i in range(len(s)-1,-1,-1):
        p+=s[i]
    return p
a=input()
st=""
m=0
for i in range(len(a)):
    s=""
    for j in range(i,len(a)):
        s+=a[j]
        if s==strrev(s):
            if s in a:
                if len(s)>m:
                    st=s
                    m=len(st)
print(st)