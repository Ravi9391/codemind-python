n=int(input())
a=list(map(int,input().split()))
x=int(input())
c=-1
d=-1
for i in range(n):
    if(a[i]==x and c==-1):
        c=i
    if a[i]==x:
        d=i
print(c,d)