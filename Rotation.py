n=int(input())
for _ in range(n):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    x=k%n
    print(*l[n-x:]+l[:n-x])