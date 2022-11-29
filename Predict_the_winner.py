n=int(input())
a=list(map(int,input().split()))
es=0
os=0
for i in range(n):
    if a[i]%2==0:
        es=es+a[i]
    else:
        os=os+a[i]
d=abs(os-es)
if d%4==0:
    print('X')
else:
    print('Y')