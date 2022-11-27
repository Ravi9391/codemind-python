def checkMajorityElement(arr,N):
    mp={}
    for i in range(0,N):
        if arr[i] in mp.keys():
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    for key in mp:
        if mp[key]>(N/2):
            return key
    return -1
N=int(input())
arr=list(map(int,input().split()))
ans = checkMajorityElement(arr,N)
if ans!=-1:
    print(ans)
else:
    print("No majority element in array")