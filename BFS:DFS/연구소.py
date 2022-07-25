#3개의 벽을 세우는 조합을 찾아 각각의 안전구역 크기 확인하기
n,m = map(int, input().split())
data = []
temp = [[0] *m for _ in range(n)]

for _ in range(n):
  data.append(list(map(int,input().split())))

#상하좌우
dx = [-1,0,1,0]
dy = [0, 1, 0,-1]

result = 0

#DFS
def virus(x,y) :
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    #바이러스가 퍼질 수 있는 경우
    if nx>= 0 and nx<n and ny>=0 and ny<m:
      if temp[nx][ny] ==0:
        #바이러스(2) 설치
        temp[nx][ny] =2
        virus(nx,ny)

#안전영역 크기 계산
def get_score():
  score =0
  for i in range(n):
    for j in range(m):
      if temp[i][j]==0:
        score+=1
  return score

#DFS 울타리 설치 + 안전 영역 크기
def dfs(count):
  global result
  #울타리 3개 설치된 경우
  if count==3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]

    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i,j)
    result = max(result, get_score())
    return

  for i in range(n):
    for j in range(m):
      if data[i][j] ==0:
        data[i][j] =1
        count+=1
        dfs(count)
        data[i][j] = 0
        count-=1

dfs(0)
print(result)