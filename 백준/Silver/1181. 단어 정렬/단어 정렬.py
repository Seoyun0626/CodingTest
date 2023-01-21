N=int(input())
word=[]
for _ in range(N):
    word.append(input())
set_list=set(word)
word=list(set_list)
word.sort()
word.sort(key=len)

for i in word:
    print(i)