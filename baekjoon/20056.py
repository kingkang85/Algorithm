# 20056. 마법사 상어와 파이어볼
'''
K번 반복
1. 위치, 질량, 속력, 합을 가지고 이동
2. 각 칸마다 두 개 이상 있는지 확인
    - 질량은 (질량합 // 5)로 저장
        - 질량이 0이 되면 없앰
    - 속력은 (속력합 // 개수)로 저장
    - 방향이 모두 짝수 or 모두 홀수 이면 => 0, 2, 4, 6으로 퍼짐
        - 아니라면 1, 3, 5, 7
남아있는 파이어볼 질량의 합은?
'''
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
fireball = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append((r-1, c-1, m, s, d))

direct = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

for _ in range(K):
    # 이동
    new_pos = {}
    for r, c, m, s, d in fireball:
        nr = (r + direct[d][0] * s) % N
        nc = (c + direct[d][1] * s) % N
        if (nr, nc) in new_pos:
            new_pos[(nr, nc)].append((m, s, d))
        else:
            new_pos[(nr, nc)] = [(m, s, d)]
            
    new_fireballs = []
    

    move2 = []
    for i in range(N):
        for j in range(N):
            n = len(arr[i][j])
            a = b = 0
            dd = []
            if n >= 2:
                print(arr[i][j])
                while arr[i][j]:
                    m, s, d = arr[i][j].pop()
                    a += m
                    b += s
                    dd.append(d)
                
                a //= 5
                b //= n

                if a == 0:
                    break

                for i in range(len(dd)):
                    dd[i] %= 2
                
                for j in range(len(dd)-1):
                    if dd[j] != dd[j+1]:
                        new_dd = [1, 3, 5, 7]
                        break

                else:
                    new_dd = [0, 2, 4, 6]
                
                for d in new_dd:
                   move2.append((i, j, a, b, d))

    for i, j, a, b, d in move2:
        arr[i][j].append((a, b, d))


result = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            while arr[i][j]:
                m, s, d = arr[i][j].pop()
                result += m
print(result)
