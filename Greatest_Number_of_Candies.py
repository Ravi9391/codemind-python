n=int(input())
a=list(map(int,input().split()))
x=int(input())
max=a[0];
for i in range(n):
    if(a[i]>max):
        max=a[i]
for i in range(n):
    check=0
    check=a[i]+x
    if(check>=max):
        print("True",end=' ')
    else:
        print("False",end=' ')