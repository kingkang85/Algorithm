# 14889. 스타트와 링크
# 능력치 계산하는 함수
def Cal(lst):
    n = len(lst)
    result = 0
    for i in range(n-1):
        for j in range(i+1, n):
            result += status[lst[i]][lst[j]] + status[lst[j]][lst[i]]
    return result

# 조합 만드는 함수
def get_comb(lev, st):
    global minV
    
    if lev == N//2:  # 개수가 N//2개가 되었을 때 중단
        teamL = [i for i in range(N) if i not in teamS]  # 링크 팀 : 스타트 팀에 없는 것들
        totalS = Cal(teamS)
        totalL = Cal(teamL)

        # 두 팀의 능력치 차이를 구한 후 최솟값 비교
        if minV > abs(totalS - totalL):
            minV = abs(totalS - totalL)
        return

    for i in range(st, N):
        if minV == 0:  # 이미 최솟값이 0이라면 중단
            return
        teamS.append(i)
        get_comb(lev + 1, i + 1)
        teamS.pop()
    

N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]

teamS = []
minV = 10e5
get_comb(0, 0)

print(minV)