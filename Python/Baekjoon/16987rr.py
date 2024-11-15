#16987. 계란으로 계란치기
'''
1. 가장 왼쪽의 계란을 든다.
2. 깨지지 않은 계란 중 하나를 친다.
    - 현재 손에 든 계란이 깨졌거나 깨지지 않은 계란이 없으면 패스
3. 다음 계란을 들고 다시 진행한다.
    - 그 전이 가장 오른쪽이었으면 종료
4. 내구도 = 내구도 - 무게
dfs에 무엇을 넘겨줄까..
현재 계란, 깨진 계란들, 내구도..
'''
import sys
input = sys.stdin.readline

def dfs(now, broken_eggs):
    global maxV

    if now == N - 1:
        maxV = max(maxV, len(broken_eggs))
        return
    
    for next in range(N):
        if next in broken_eggs or now == next:
            continue

        if now in broken_eggs or len(broken_eggs) == N-1:
            dfs(now + 1, broken_eggs)
            return

        eggs[now][0] -= eggs[next][1]
        eggs[next][0] -= eggs[now][1]

        if eggs[now][0] <= 0:
            broken_eggs.append(now)
        if eggs[next][0] <= 0:
            broken_eggs.append(next)
        
        dfs(now + 1, broken_eggs)

        eggs[now][0] += eggs[next][1]
        eggs[next][0] += eggs[now][1]

        if eggs[now][0] - eggs[next][1] < 0:
            broken_eggs.pop()
        if eggs[next][0] - eggs[now][1] < 0:
            broken_eggs.pop()

    return

N = int(input())
eggs = []
for _ in range(N):
    eggs.append(list(map(int, input().split())))

maxV = 0
dfs(0, [])
print(maxV)