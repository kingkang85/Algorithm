# 5644. [모의 SW 역량테스트] 무선 충전
from collections import deque
def MakeBC(stx, sty, C, P, num):
    dq = deque()
    visited = [[0] * 10 for _ in range(10)]

    dq.append((sty, stx, 0))
    visited[sty][stx] = 1
    arr[sty][stx].append((P, num))

    while dq:
        r, c, dist = dq.popleft()
        if dist ==  C:
            return
        
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            newr, newc = r + dr, c + dc
            if 0 <= newr < 10 and 0 <= newc < 10 and visited[newr][newc] == 0:
                dq.append((newr, newc, dist + 1))
                visited[newr][newc] = 1
                arr[newr][newc].append((P, num))


T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    userA = [0] + list(map(int, input().split()))
    userB = [0] + list(map(int, input().split()))
    BC_info = [list(map(int, input().split())) for _ in range(A)]

    # 배열에 충전 정보 저장
    arr = [[[] for _ in range(10)] for _ in range(10)]
    for i in range(A):
        MakeBC(BC_info[i][0] - 1, BC_info[i][1] - 1, BC_info[i][2], BC_info[i][3], i)
    
    # 성능 좋은 순으로 정렬
    for i in range(10):
        for j in range(10):
            arr[i][j].sort(reverse=True)

    direction = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]

    rA = cA = 0
    rB = cB = 9
    maxV = 0

    # 이동시키면서 최대 충전값 찾기
    for i in range(M+1):
        rA += direction[userA[i]][0]
        cA += direction[userA[i]][1]
        rB += direction[userB[i]][0]
        cB += direction[userB[i]][1]

        # A에는 있고 B에는 없을 때
        if arr[rA][cA] and not arr[rB][cB]:
            maxV += arr[rA][cA][0][0]
        
        # B에는 있고 A에는 없을 때
        elif arr[rB][cB] and not arr[rA][cA]:
            maxV += arr[rB][cB][0][0]
        
        # A, B 둘 다 있을 때
        elif arr[rA][cA] and arr[rB][cB]:
            # 둘이 같은 BC일 때
            if arr[rA][cA][0][1] == arr[rB][cB][0][1]:
                maxV += arr[rA][cA][0][0]  # 여기서 반씩 나눠가지는 경우도 처리됨

                # 둘 다 다른 경로가 있을 때
                if len(arr[rA][cA]) > 1 and len(arr[rB][cB]) > 1:
                    maxV += max(arr[rA][cA][1][0], arr[rB][cB][1][0])
                # A만 다른 경로가 있을 때
                elif len(arr[rA][cA]) > 1:
                    maxV += arr[rA][cA][1][0]
                # B만 다른 경로가 있을 때
                elif len(arr[rB][cB]) > 1:
                    maxV += arr[rB][cB][1][0]
            
            # 다른 BC일 때
            else:
                maxV += arr[rA][cA][0][0] + arr[rB][cB][0][0]

    print(f'#{tc} {maxV}')