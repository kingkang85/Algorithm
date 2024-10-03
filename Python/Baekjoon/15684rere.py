# 15684. 사다리 조작
# 5:25까지
# i번이 i번으로 나오도록 잘 조작되었는지 확인하는 함수
def Check():
    for col in range(N):
        nr = arr[0][col][0]
        nc = col + arr[0][col][1]

        while nr < H - 1:
            nr = arr[nr][nc][0]
            nc = arr[nr][nc][1]
        
        if nc != col:
            return False
        
    return True
            

N, M, H = map(int, input().split())
arr = [[(1, 0)] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = (1, 1)
    arr[a-1][b] = (1, -1)
 
# 사다리 후보군 뽑기..
ladder_lst = []
for i in range(H):
    for j in range(N-1):
        if arr[i][j] == (1, 0):
            for di, dj in [[0, -1], [0, 1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and arr[ni][nj] == (1, 1):
                    break
            else:
                ladder_lst.append((i, j))
                    
print(ladder_lst)

# print(arr)
# print(Check())