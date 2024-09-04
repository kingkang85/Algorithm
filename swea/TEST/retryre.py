# 4014. 활주로 건설
def check():
    cnt = 0
    for i in range(N):
        for j in range(N-1):
            if ground[i][j] > ground[i][j+1]:
                cnt += 1
    if cnt > X:
        total += 1 

        for j in range(N-1):
            # if ground[j][i] < ground[j][i-]:
                pass        


T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())

    ground = [list(map(int, input().split())) for _ in range(N)]
  