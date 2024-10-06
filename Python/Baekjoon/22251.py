# 22251. 빌런 호석
import sys
input = sys.stdin.readline

def dfs(dep, cnt, floor):
    # 종료 조건
    if dep == len(floor):
        if int(floor) == X:
            return 0
        elif 1 <= int(floor) <= N:
            return 1
        else:
            return 0
    
    result, cur = 0, int(floor[dep])
    for i in range(10):
        # 현재 숫자와 다른 경우
        if cur!= i and arr[cur][i] <= cnt:
            new_floor = floor[:dep] + str(i) + floor[dep+1:]
            result += dfs(dep+1, cnt-arr[cur][i], new_floor)
        
        # 현재 숫자와 같은 경우
        elif cur == i:
            result += dfs(dep+1, cnt, floor)  # 변경 없이 다음 자릿수로 dfs 호출
    
    return result


N, K, P, X = map(int, input().split())

num = ['1111110', '0110000', '1101101', '1111001', '0110011',
       '1011011', '1011111', '1110000', '1111111', '1111011']

# 자릿수 맞추기
if K > len(str(X)):
    floor = '0' * (K - len(str(X))) + str(X)
else:
    floor = str(X)

# 각 숫자를 다른 숫자로 바꿀 때 반전시켜줘야 하는 LED 개수
arr = [[0] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if i != j:
            change = 0
            for k in range(7):
                if num[i][k] != num[j][k]:
                    change +=1
            arr[i][j] = change

print(dfs(0, P, floor))