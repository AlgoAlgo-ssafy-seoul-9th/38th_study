import sys
input = sys.stdin.readline

arr = input().strip()
n = len(arr)
palin = [[0] * n for _ in range(n)]     # palin[i][j] : i부터 j번쩨까지의 문자열 중 팰린드롬 분할 최소 수 

# 길이가 1인 문자열은 모두 팰린드롬
for i in range(n):
    palin[i][i] = 1

# 길이가 2인 문자열은 다음 꺼랑 같은지로 팰린드롬
for i in range(n-1):
    if arr[i] == arr[i+1]:
        palin[i][i+1] = 1

# 길이가 3 이상인 문자열
for length in range(3, n+1):    
    for i in range(n-length+1):
        j = i + length -1
        if arr[i] == arr[j] and palin[i+1][j-1]:
            palin[i][j] = 1
# print(palin)
print(palin[0][n-1])
