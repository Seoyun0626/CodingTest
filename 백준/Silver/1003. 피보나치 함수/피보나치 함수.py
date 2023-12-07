def fib(N):
    zeros = [1,0,1]
    ones = [0,1,1]
    if (N >= 3):
        for i in range(2, N):
            zeros.append(zeros[i] + zeros[i - 1])
            ones.append(ones[i] + ones[i - 1])
    print(zeros[N], ones[N])

T = int(input())
for _ in range(T):
    N = int(input())
    fib(N)



