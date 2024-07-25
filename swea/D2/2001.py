# 2001. 파리 퇴치
T = int(input())
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # N x N 배열

result = []
for i in range(N-M+1):
    for j in range(N-M+1):
        print(arr[i][j])
