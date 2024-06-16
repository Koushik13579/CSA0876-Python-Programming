import heapq
def swimInWater(grid):
    n = len(grid)
    pq = [(grid[0][0], 0, 0)]
    visited = {(0, 0)}
    while pq:
        t,x,y=heapq.heappop(pq)
        if (x,y) == (n - 1, n - 1):
            return t
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                heapq.heappush(pq, (max(t, grid[nx][ny]), nx, ny))
grid=[[2,4],[2,3]]
print(swimInWater(grid))