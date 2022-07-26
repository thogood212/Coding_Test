# 너비우선검색
#nxn 크기
#k개 바이러스
#S 초단위
#x,y의 좌표
from collections import deque

n, k = map(int,input().split())

graph =[] #전체 보드 정보
data = [] #바이러스 정보

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(n):
  graph.append(list(map(int,input().split())))
  for j in range(n):
    #바이러스 존재하는 경우
    if graph[i][j]!=0 :
      data.append((graph[i][j],0, i, j))

#낮은 번호 바이러스 부터 증식
data.sort()
q = deque(data)

ta_s, ta_x, ta_y = map(int,input().split())

#BFS 진행
while q:
  virus, s, x, y = q.popleft()
  # s초가 지나거나, 큐가 빌때까지 진행
  if s == ta_s:
    break
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx>=0 and nx<n and ny>=0 and ny<n:
      if graph[nx][ny]==0:
        graph[nx][ny] = virus
        q.append((virus, s+1, nx,ny))

print(graph[ta_x-1][ta_y-1])