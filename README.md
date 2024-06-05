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

```

### [상미](./기타줄/상미.py)

```py

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
₩
```py
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
