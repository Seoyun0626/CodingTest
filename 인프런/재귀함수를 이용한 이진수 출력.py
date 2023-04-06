n = int(input())

def bi_num(x):
    if x != 0:
        bi_num(x // 2)
        print(x % 2, end="")

bi_num(n)