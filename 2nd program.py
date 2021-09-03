print("Enter array elements: ",end='')
arr=list(map(int,input().split()))
su=int(input("Enter Sum: "))
for i in range (0,len(arr)):
    for j in range(i,len(arr)):
        if arr[i]+arr[j]==su:
            print(arr[i],arr[j],sep=',')
            exit(0)
print("No Pairs Found")