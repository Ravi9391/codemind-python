n=int(input())
l=[]
k=[]
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(n):
    b=int(input())
    k.append(b)
c=0
for i in range(n):
    f=0
    for j in range(n):
        if l[i]<=k[j]:
            k[j]=0
            f=1
            break
    if f==0:
        c+=1
print(c)