# 17135. 캐슬 디펜스
import sys, copy
input = sys.stdin.readline

# 게임이 끝났는지 확인하는 함수
def check(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                return False
    return True

# 적 이동 함수
def change(arr):
    for i in range(N-1, 0, -1):
        arr[i][:] = arr[i-1][:]
    arr[0][:] = [0] * M

# 가장 가까운 적 찾는 함수
def get_target(r, c, arr):
    min_dist = D + 1
    target = None

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                dist = abs(r-i) + abs(c-j)
                if dist <= D:
                    # 가장 가까운 적 찾기
                    if dist < min_dist:
                        min_dist = dist
                        target = (i, j)
                    # 거리가 같은 경우 가장 왼쪽에 있는 적 찾기
                    elif dist == min_dist and j < target[1]:
                        target = (i, j)
    
    return target

# 궁수 조합 & 게임 진행 함수
def attack(lev, st):
    global maxCnt
    if lev == 3:
        current_map = copy.deepcopy(arr) # 맵 복사
        cnt = 0
        
        # 적이 없을 때까지 게임 진행
        while not check(current_map):
            targets = set()
            for col in starts:
                target = get_target(N, col, current_map)
                if target:
                    targets.add(target)
            
            # 공격!!!
            for tr, tc in targets:
                current_map[tr][tc] = 0
                cnt += 1
            
            # 공격 후 적 이동
            change(current_map)
        
        maxCnt = max(maxCnt, cnt)
        return

    for i in range(st, M):
        if not used[i]:
            starts.append(i)
            used[i] = 1
            attack(lev+1, i+1)
            starts.pop()
            used[i] = 0


N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
starts = []
used = [0] * M
maxCnt = 0
attack(0, 0)
print(maxCnt)