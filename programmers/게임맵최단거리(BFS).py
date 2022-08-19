from collections import deque

def solution(maps):
    answer = 1
    n = len(maps)
    m = len(maps[0])
    
    #하,우,상,좌
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
        
    q= deque([(0,0,0)])
    
    maps[0][0]=0
    
    while q:
        x, y, t = q.popleft()
        if x==n-1 and y==m-1:
            break

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and maps[nx][ny]==1:
                    maps[nx][ny]=0
                    q.append((nx,ny, t+1))
                    
                    
    if x!=n-1 or y!=m-1:
        return -1 
        
    return t+1