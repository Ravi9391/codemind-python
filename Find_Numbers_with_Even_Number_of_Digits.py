def digits(n):
    c=0
    while n!=0:
        i=n%10
        n=n//10
        c+=1
    return c
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if digits(a[i])%2==0:
        c+=1
print(c)