word=input()
n=len(word)
t=(n//10)+1
p=(n%10)
for i in range(t):
    if(i!=t-1):
        for s in range(i*10,(i*10)+10):
            print(word[s],end="")
        print()
    else:
        for s in range(i*10,(i*10)+p):
            print(word[s],end="")