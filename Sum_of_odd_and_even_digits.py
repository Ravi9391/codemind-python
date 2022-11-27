n=int(input())
a=list(map(int,input().split()))
s=0
sum=0
for i in range(n):
    if i%2==0:
        s=s+a[i]
for i in range(n):
    if i%2!=0:
        sum=sum+a[i]
if s==sum:
    print('YES')
else:
    print('NO')