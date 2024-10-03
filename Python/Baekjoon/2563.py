# 2563. 색종이
N = int(input())
arr = [[0] * 100 for _ in range(100)]

for _ in range(N):
    r, c = map(int, input().split())

    # 주어진 범위만큼 도화지 색칠
    for i in range(r, r+10):
        arr[i][c:c+10] = [1] * 10

# arr의 1의 개수가 검은색의 넓이
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)