n=int(input())
a=list(map(int,input().split()))
for i in a:
    if a.count(i)==1:
        pass
    else:
        print(i)
        break