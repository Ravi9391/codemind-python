x=int(input())
for i in range(x):
    n=int(input())
    c=1
    a=list(map(int,input().split()))
    for i in range(n-1):
        if a[i+1]<a[i]:
            c+=1
    print(c)