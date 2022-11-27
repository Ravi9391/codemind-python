n=int(input())
a=list(map(int,input().split()))
s=[]
for i in range(n):
    s.append(a[i]*a[i])
s=sorted(s)
for j in s:
    print(j,end=' ')