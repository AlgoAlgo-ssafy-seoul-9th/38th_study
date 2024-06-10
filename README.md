# 38st_study

알고리즘 스터디 38주차

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [기타줄](https://www.acmicpc.net/problem/1049)

### [민웅](./기타줄/민웅.py)

```py
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
```

### [상미](./기타줄/상미.py)

```py
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

```

### [성구](./기타줄/성구.py)

```py
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

```

### [영준](./기타줄/영준.py)

```py

```

<br/>

## [귀도 반 로썸은 크리스마스날 심심하다고 파이썬을 만들었다](https://www.acmicpc.net/problem/6568)

### [민웅](./귀도%20반%20로썸은%20크리스마스날%20심심하다고%20파이썬을%20만들었다/민웅.py)

```py
# 6568_귀도 반 로썸은 크리스마스날 심심하다고 파이썬을 만들었다.
import sys
input = sys.stdin.readline

while True:
    base = []
    is_end = False
    for i in range(32):
        tmp = input().strip()
        base.append(tmp)
        if not tmp:
            is_end = True
            break
    if is_end:
        break
        
    adder = 0
    pc = 0

    while True:
        tmp = base[pc]
        o_type = tmp[:3]
        address = tmp[3:]

        # 5비트짜리
        pc = (pc + 1) % 32
        o_type = int(o_type, 2)
        # print(tmp, o_type, address)
        if o_type == 0:
            base[int(address, 2)] = bin(adder)[2:].zfill(8)
        elif o_type == 1:
            adder = base[int(address, 2)]
            adder = int(adder, 2)
        elif o_type == 2:
            if adder == 0:
                pc = int(address, 2)
        elif o_type == 3:
            continue
        elif o_type == 4:
            adder -= 1
        elif o_type == 5:
            adder += 1
        elif o_type == 6:
            pc = int(address, 2)
        else:
            break

        # 8비트짜리
        adder = adder % 256

    print(bin(adder)[2:].zfill(8))

```

### [상미](./귀도%20반%20로썸은%20크리스마스날%20심심하다고%20파이썬을%20만들었다/상미.py)

```py

```

### [성구](./귀도%20반%20로썸은%20크리스마스날%20심심하다고%20파이썬을%20만들었다/성구.py)

```py

```

### [영준](./귀도%20반%20로썸은%20크리스마스날%20심심하다고%20파이썬을%20만들었다/영준.py)

```py

```

<br/>

## [팰린드롬 분할](https://www.acmicpc.net/problem/1509)

### [민웅](./팰린드롬%20분할/민웅.py)

```py
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
```

### [상미](./팰린드롬%20분할/상미.py)

```py

```

### [성구](./팰린드롬%20분할/성구.py)

```py

```

### [영준](./팰린드롬%20분할/영준.py)

```py

```

<br/>

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

<br/>

## [도넛과 막대 그래프](https://school.programmers.co.kr/learn/courses/30/lessons/258711)

### [민웅](./도넛과%20막대%20그래프/민웅.py)

```py
from collections import deque
def solution(edges):
    adjL = [[] for _ in range(1000001)]
    in_info = {}
    out_info = {}
    main_node = -1
    for e in edges:
        if e[0] in in_info.keys():
            in_info[e[0]] += 1
        else:
            in_info[e[0]] = 1
        
        if main_node == -1 or in_info[e[0]] >= 2:
            if e[0] not in out_info.keys():
                main_node = e[0]
            
        if e[1] in out_info.keys():
            out_info[e[1]] -= 1
        else:
            out_info[e[1]] = -1
        
        adjL[e[0]].append(e[1])
    
    D, M, E = 0, 0, 0
    for n in adjL[main_node]:
        q = deque()
        is_cycle = False
        is_double = False
        is_self = False
        q.append(n)
        visited = set()
        visited.add(n)
        while q:
            now = q.popleft()
            
            if len(adjL[now]) > 1:
                is_double = True
                break
            for node in adjL[now]:
                if node == now:
                    D += 1
                    is_self = True
                    break
                if node not in visited:
                    visited.add(node)
                    q.append(node)
                else:
                    is_cycle = True
                    break
                    
        if not is_cycle and not is_double and not is_self:
            M += 1
            # print("M", n, M)
        if is_cycle and not is_double and not is_self:
            D += 1
            # print("D", n, D)
        if is_double:
            E += 1
            # print("E", n, E)
                    
    answer = [main_node, D, M, E]
    return answer
```

### [상미](./도넛과%20막대%20그래프/상미.py)

```py

```

### [성구](./도넛과%20막대%20그래프/성구.py)

```py
from collections import defaultdict

def solution(edges):
    answer = [0] * 4

    def dfs(start):
        stack = [(start)]
        v = set()
        while stack:
            spot = stack.pop()

            # 중간 출력 간선이 2개 이상이면 8자
            if len(graph[spot]) > 1:
                return 3

            for node in graph[spot]:
                # 처음으로 돌아오면 도넛
                if node == start:
                    return 1

                v.add(node)
                stack.append(node)
        # 모두 돌고 나오면 막대
        return 2


    # 그래프 세팅
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)

    visited = set()
    nodes = set()

    # 입력 간선이 없는 노드를 찾기 위한 set 연산
    for node, posts in graph.items():
        visited.update(posts)
        nodes.add(node)

    addi_node = tuple(nodes - visited)

    # 만약 여러 개라면 출력 간선이 2개 이상이 노드
    for n in addi_node:
        if len(graph[n]) > 1:
            target = n

    answer[0] = target

    # 필터링
    for start in graph[target]:
        answer[dfs(start)] += 1


    return answer
```

### [영준](./도넛과%20막대%20그래프/영준.py)

```py

```

</details>

<br/><br/>

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

</details>
