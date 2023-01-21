L=int(input())
word=input()
result=0
for i in range(L):
    num=ord(word[i])-96
    result+=num*(31**i)
print(result)