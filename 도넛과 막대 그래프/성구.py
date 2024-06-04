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
        # 모두 돌고 나오면 
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