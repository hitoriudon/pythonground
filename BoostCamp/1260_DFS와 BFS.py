n, m, v = map(int,input().split())
matrix = [[0]*(n+1) for _ in range (n+1)] #2차원 배열 선언 빠르게
for i in range (m):
    a, b = map(int, input().split()) #input method
    matrix[a][b] = matrix[b][a] = 1 #연결 표시
visited = [0 for _ in range (n+1)]

def dfs(v):
    visited[v] = 1 #방문 표시
    print(v, end=" ") #출력
    for i in range (1, n+1):
        if visited[i]==0 and matrix[v][i]==1:
            dfs(i)
            
def bfs(v):
    queue = [v]
    visited[v] = 0 #dfs 결과로 다 1로 바뀌어져있음. 뒤집어주기
    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for i in range (1, n+1):
            if visited[i]==1 and matrix[v][i] == 1:
                queue.append(i)
                visited[i] = 0
dfs(v)
print()
bfs(v)