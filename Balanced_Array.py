x=int(input())
for i in range(x):
    n=int(input())
    c=0
    a=list(map(int,input().split()))
    for i in range(n):
        if sum(a[:i])==sum(a[i+1:]):
            c=1
    if c==1:
        print('YES')
    else:
        print('NO')