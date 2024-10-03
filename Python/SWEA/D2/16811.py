# 16811. 당근 포장하기
# 당근 개수 차이 return
def cal(m_s, m_e):
    small = sum(counts[minC:m_s])
    medium = sum(counts[m_s:m_e+1])
    large = sum(counts[m_e+1:maxC+1])

    if small == 0 or medium == 0 or large == 0:
        return -1
    if small > N//2 or medium > N//2 or large > N//2:
        return -1

    return max(small, medium, large) - min(small, medium, large)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))

    counts = [0] * 31
    for c in carrot:
        counts[c] += 1

    minC = min(carrot)
    maxC = max(carrot)
    minV = 1001
    for m_s in range(minC + 1, maxC):  # 중간 박스가 시작할 수 있는 곳
        for m_e in range(m_s, maxC):  # 중간 박스가 끝날 수 있는 곳
            t = cal(m_s, m_e)

            if t == -1:
                continue

            if minV > t:
                minV = t

    if minV == 1001:  # minV가 그대로이면 만족 X
        minV = -1

    print(f'#{tc} {minV}')