# 1049_기타줄_guitar string
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

p_min, o_min = 1001, 1001

for _ in range(M):
    pack, one = map(int, input().split())
    p_min = min(p_min, pack)
    o_min = min(o_min, one)

# print(N//6, N%6)
ans = min(((N//6)+1)*p_min, (N//6)*p_min + (N%6)*o_min, o_min*N)

print(ans)