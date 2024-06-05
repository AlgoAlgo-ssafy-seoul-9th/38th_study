# 1049 기타줄
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 최소 저장용
min_six, min_one = 10001, 10001

# 최소 비교
for _ in range(M):
    six, one = map(int, input().split())

    min_six = min(six, min_six)
    min_one = min(one, min_one)

# 그리디 조건
if min_one*6 < min_six:
    # 하나씩 사는게 무조건 작으면 비교할 필요 없음
    print(N * min_one)
else:
    # 6개 세트가 더 쌀 때 비교
    cost = 0
    # 6개 이상일 땐 6개 사는게 무조건 이득
    while N >= 6:
        cost += min_six
        N -= 6

    # 6개 미만일 때 비교
    if min_one * N < min_six:
        print(cost+min_one*N)
    else:
        print(cost+min_six)
            