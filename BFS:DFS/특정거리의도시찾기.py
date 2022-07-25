#그래프에서 모든 간선의 비용이 동일하면 BFS(너비우선탐색)을 이용하여 최단거리 검색
from collections import deque

n,m,k,x= map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)

#모든 도시 최단 거리 초기화
distance = [-1]*(n+1)
distance[x] = 0

#너비 우선 탐색 실행
q = deque([x])

while q:
  now = q.popleft()
  # 이동할 수 있는 도시 확인
  for next_node in graph[now]:
    #방문하지 않은도시  
    if distance[next_node]==-1:
      distance[next_node] = distance[now]+1
      q.append(next_node)

#최단 거리 K인 모든 도시의 번호를 오름차순 출력
check = False
for i in range(1,n+1):
  if distance[i] ==k:
    print(i)
    check = True

if check == False:
  print(i)
