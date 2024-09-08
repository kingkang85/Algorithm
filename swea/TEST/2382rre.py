# 2382. [모의 SW 역량테스트] 미생물 격리
# 4:12 ~

'''
1. 구역 배열 만들기 (가장자리는 -1)
    - 미생물 배치 (미생물 수와 이동 방향 저장)
2. 미생물 움직이는 함수 만들기 (M번 반복)
    - 미생물이 있는 곳을 찾아서 새로운 배열로 이동시키기
    - 움직인 곳이 -1이면 미생물 수 절반, 방향 반대로
    - 움직인 곳에 이미 미생물이 있으면 미생물 수 비교 후 방향 설정, 미생물 수 합치기
    - 새로운 배열 return
3. 남아있는 미생물의 총 개수 출력
'''
import sys
sys.stdin = open('input.txt', 'r')
def Move(arr):
    tmp = [[-1] * N] + [[-1] + [0] * (N-2) + [-1] for _ in range(N-2)] + [[-1] * N]
    d = [0, [-1, 0], [1, 0], [0, -1], [0, 1]]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == -1 or arr[i][j] == 0:
                continue
            
            cnt, way = arr[i][j]
            ni = i + d[way][0]
            nj = j + d[way][1]

            if 0 <= ni < N and 0 <= nj < N:
                if tmp[ni][nj] == -1:
                    cnt //= 2
                    if way in {1, 2}:
                        way = 3 - way
                    else:
                        way = 7 - way
                    
                    if cnt == 0:
                        continue
                
                elif tmp[ni][nj]:
                    new_cnt, new_way = tmp[ni][nj]
                    if new_cnt > cnt:
                        cnt, way = new_cnt + cnt, new_way
                    else:
                        cnt += new_cnt

                tmp[ni][nj] = [cnt, way]

    return tmp
                

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    arr = [[-1] * N] + [[-1] + [0] * (N-2) + [-1] for _ in range(N-2)] + [[-1] * N]
    for _ in range(K):
        r, c, num, direct = map(int, input().split())
        arr[r][c] = [num, direct]

    for _ in range(M):
        arr = Move(arr)

    total = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -1 or arr[i][j] == 0:
                continue
            total += arr[i][j][0]

    print(f'#{tc} {total}')