# 15649. N과 M (1)
def perm(lev):
    if lev == M:
        print(*path)
        return
    
    for i in range(1, N+1):
        if not used[i]:
            path.append(i)
            used[i] = 1  # 사용 표시
            perm(lev + 1)
            path.pop()
            used[i] = 0  # 복원
           
N, M = map(int, input().split())
path = []
used = [0] * (N+1)
perm(0)