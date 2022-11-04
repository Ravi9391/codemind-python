n=int(input())
l=[]
a=2
b=2
r=0
for i in range(n):
    l.append(a)
    r=a+b
    a=b
    b=r
print(l[n-1])