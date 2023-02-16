#bfs문제

from collections import deque

def solution(maps):
    answer = []
    visited=[[0]*(len(maps[0])) for _ in range(len(maps))]

    def bfs(x,y):
        q=deque()
        q.append((x,y))
        visited[x][y]=1
        days=0
        dx=[1,-1,0,0]
        dy=[0,0,1,-1]
        while q:
            a,b=q.popleft()
            days+=int(maps[a][b])
            for i in range(4):
                na=a+dx[i]
                nb=b+dy[i]
                if 0<=na<len(maps) and 0<=nb<len(maps[0]) and visited[na][nb]==0 and maps[na][nb]!='X':
                    visited[na][nb]=1
                    q.append((na,nb))
        answer.append(days)


    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]!='X' and visited[i][j]==0:
                print(i,j)
                bfs(i,j)
    if answer:
        return sorted(answer)
    else:
        return [-1]