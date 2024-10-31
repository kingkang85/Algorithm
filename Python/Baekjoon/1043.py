# 1043. 거짓말
import sys
input = sys.stdin.readline

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if px in know and py in know:
        return

    if px in know:
        p[py] = px

    elif py in know:
        p[px] = py

    # 둘 다 진실을 모르는 경우
    else:
        if px < py:
            p[py] = px
        else:
            p[px] = py

N, M = map(int, input().split())
know = list(map(int, input().split()[1:]))  # 진실을 아는 사람들

p = [i for i in range(N+1)]
parties = []

# 진실을 아는 사람들 / 모르는 사람들 묶기
for _ in range(M):
    info = list(map(int, input().split()))
    ppl = info[0]
    party = info[1:]

    for i in range(ppl-1):
        union(party[i], party[i+1])

    parties.append(party)

result = 0
for party in parties:
    for i in range(len(party)):
        # 파티원 중에 진실을 아는 사람이 있다면 종료
        if find(party[i]) in know:
            break
    else:
        result += 1
print(result)