from itertools import permutations
arr=["Subject1","Subject2","Subject3","Subject4","Subject5"]
#hour=["\t\t\t        \t\t\tFirst Hour","Second Hour","Third Hour","Fourth Hour","Fifth Hour"]
san=set(permutations(arr,5))
c=1
#print(*hour)
for i in san:
    if c<6:
        print("Day"+str(c)+" :",end=' ')
        print(*i,sep=' ',end=' ')
        print()
        c+=1