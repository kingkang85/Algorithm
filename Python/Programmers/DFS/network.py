# 네트워크
def dfs(n, computers, com, visited):
    visited[com] = 1

    for i in range(n):
        if i != com and computers[i][com] == 1 and visited[i] == 0:
            dfs(n, computers, i, visited)

def solution(n, computers):
    visited = [0] * n
    answer = 0

    for com in range(n):
        if visited[com] == 0:
            dfs(n, computers, com, visited)
            answer += 1

    return answer