s=0;
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(n):
        if(a[i]==a[j]):
            c+=1
    if(c==1):
        s=1
        print(a[i],end=' ')
if(s==0):
    print("-1")