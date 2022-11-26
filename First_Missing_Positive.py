n=int(input())
a=list(map(int,input().split()))
for i in range(1,1000):
    if i not in a:
        print(i)
        break