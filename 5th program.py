word1=input("Word-1: ").strip()
word2=input("Word-2: ").strip()
for i in word1:
    if i not in word2:
        print(i,end='')
for i in word2:
    if i not in word1:
        print(i,end='')