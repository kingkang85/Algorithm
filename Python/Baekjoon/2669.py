# 2669. 직사각형 네 개의 합집합의 면적 구하기
arr = [[0] * 100 for _ in range(100)]

for _ in range(4):
    r1, c1, r2, c2 = map(int, input().split())

    # 주어진 행과 열을 범위로 1씩 더해줌
    for r in range(r1, r2):
        for c in range(c1, c2):
            arr[r][c] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] >= 1:  # 1 이상이면 면적에 포함
            cnt += 1

print(cnt)
