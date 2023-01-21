import sys
N=int(sys.stdin.readline())
inf=[]
for i in range(N):
    inf.append(list(sys.stdin.readline().split()))
inf.sort(key=lambda x:int(x[0]))

for i in inf :
    print(i[0],i[1])