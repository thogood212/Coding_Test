INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에게 가는 값 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

#간선 정보 확인(비용이 1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1

# 플로이드 워셜 알고리즘
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result=0

#학생 번호에 따라 확인하여 도달 가능한지 체크
for i in range(1,n+1):
    count=0
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count +=1
    if count ==n:
        result+=1
        
print(result)