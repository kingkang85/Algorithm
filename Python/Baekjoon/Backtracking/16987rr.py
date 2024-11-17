#16987. 계란으로 계란치기
import sys
input = sys.stdin.readline

def dfs(now):
    global maxV

    if now == N:
        cnt = 0
        for egg in eggs:
            if egg[0] <= 0:
                cnt += 1
        maxV = max(maxV, cnt)
        return
    
    # 현재 계란이 깨졌으면 다음으로
    if eggs[now][0] <= 0:
        dfs(now + 1)
        return
    
    # 아직 안 깨진 계란이 있는지 확인하여 다 깨졌다면 다음으로
    found = False
    for i in range(N):
        if i != now and eggs[i][0] > 0:
            found = True
            break
    
    if not found:
        dfs(now + 1)
        return
    
    for next in range(N):
        # 현재이거나 다음 계란이 깨졌다면 패스
        if now == next or eggs[next][0] <= 0:
            continue
        
        eggs[now][0] -= eggs[next][1]
        eggs[next][0] -= eggs[now][1]

        dfs(now + 1)

        eggs[now][0] += eggs[next][1]
        eggs[next][0] += eggs[now][1]
    

N = int(input())
eggs = []
for _ in range(N):
    eggs.append(list(map(int, input().split())))

maxV = 0
dfs(0)
print(maxV)