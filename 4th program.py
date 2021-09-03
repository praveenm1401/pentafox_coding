s=input("Enter The String: ").strip()
i=0
while i<len(s)-1:
    c=1
    while s[i]==s[i+1]:
        i+=1
        c+=1
        if i+1==len(s):
            break
    if c==1 and s[i]!='':
        print(s[i],end="")
    else:
        print(str(s[i])+str(c),end="")
    i+=1