# 13976. 기지국
# 주변에 기지국이 있으면 False, 없으면 True 리턴
def Check(i, j, di, dj):
    check = {1: ['A', 'B', 'C'], 2: ['B', 'C'], 3: ['C']}
    
    for dist, wifi in check.items():
        ni = i + di * dist
        nj = j + dj * dist

        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] in wifi:
            return False
    
    return True
                        

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [input() for _ in range(n)]
    
    cnt = 0
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                for k in range(4):
                    if not Check(i, j, di[k], dj[k]):
                        break
                else:  # 모든 방향에 기지국이 없으면 cnt 1 증가
                    cnt += 1

    print(f'#{tc} {cnt}')
    