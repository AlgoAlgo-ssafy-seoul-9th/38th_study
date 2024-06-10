# 1509_팰린드롬 분할_palindrome division
import sys
input = sys.stdin.readline

palin = input().strip()
l = len(palin)
dp = [[0]*l for _ in range(l)]

for i in range(l):
    dp[i][i] = 1

for i in range(2, l+1):
    for sta in range(l-i+1):
        end = sta + i - 1
        if end == sta+1:
            if palin[sta] == palin[end]:
                dp[sta][end] = 1
        if palin[sta] == palin[end]:
            if dp[sta+1][end-1]:
                dp[sta][end] = 1

dp_ans = [2501]*l

for i in range(l):
    if dp[0][i]:
        dp_ans[i] = 1

    for j in range(i):
        if dp[j+1][i]:
            dp_ans[i] = min(dp_ans[i], dp_ans[j]+1)

print(dp_ans[-1])