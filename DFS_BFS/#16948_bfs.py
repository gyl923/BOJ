import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,cnt):
    q = deque()
    q.append((x,y,cnt))
    map[x][y] = 1
    min_val = 5000
    while q:
        x,y,cnt = q.popleft()
        if x == x2 and y == y2:
            min_val = min(min_val,cnt)
            return min_val
        for i in range(6):
            X = x + dir[i][0]
            Y = y + dir[i][1]
            if 0 <= X < n and 0 <= Y < n and map[X][Y] == 0:
                q.append((X,Y,cnt+1))
                map[X][Y] = 1

    return -1