import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sixes = []
ones = []
for _ in range(M):
    six, one = map(int, input().split())
    sixes.append(six)
    ones.append(one)
    sixes.append(one*6)
sixes.sort()
ones.sort()
tmp = 0
while N > 0:
    if N >= 6:
        N -= 6
        tmp += sixes[0]
    else:
        if ones[0]*N < sixes[0]:
            tmp += ones[0]*N
        else:
            tmp += sixes[0]
        N = 0
print(tmp)


