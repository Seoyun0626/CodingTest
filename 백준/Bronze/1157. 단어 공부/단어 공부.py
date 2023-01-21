word=input()
length=len(word)
alphabet=[0]*26
word=word.upper()
for i in range(length):
    num=ord(word[i])-65
    alphabet[num]+=1
rest_alphabet=list(filter(lambda x:alphabet[x]==max(alphabet),range(len(alphabet))))

if(len(rest_alphabet)>=2):
    print('?')
else:
    print(chr(alphabet.index(max(alphabet))+65))