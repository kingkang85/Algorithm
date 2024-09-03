# 14888. 연산자 끼워넣기
def dfs(idx, midV):
    global minV, maxV
    # 모든 연산이 끝나면 중단
    if idx == N - 1:
        # 현재 계산된 중간값과 비교
        minV = min(minV, midV)
        maxV = max(maxV, midV)
        return

    for i in range(4):
        # 연산자가 있을 때만 진행
        if ops[i] > 0:
            ops[i] -= 1  # 연산자 사용
            if i == 0:  # +
                dfs(idx + 1, midV + nums[idx + 1])
            elif i == 1:  # -
                dfs(idx + 1, midV - nums[idx + 1])
            elif i == 2:  # *
                dfs(idx + 1, midV * nums[idx + 1])
            else:  # /
                dfs(idx + 1, int(midV / nums[idx + 1]))
            ops[i] += 1  # 연산자 복구


N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

minV = 10e10
maxV = -10e10
dfs(0, nums[0])  # 첫 번째 숫자부터 시작

print(maxV)
print(minV)


##########################################################################################
# 시초 코드
# def Cal(v1, v2, op):
#     if op == '+':
#         return v1 + v2
#     elif op == '-':
#         return v1 - v2
#     elif op == '*':
#         return v1 * v2
#     else:
#         return int(v1/v2)

# def perm(lev):
#     if lev == N-1:
#         tmp = nums[:]
#         for i in range(N - 1):
#             v1 = tmp.pop(0)
#             v2 = tmp.pop(0)
#             tmp = [Cal(v1, v2, path[i])] + tmp
#         calculated.append(tmp.pop())
#         return

#     for i in range(N-1):
#         if used[i] == 1:
#             continue
#         used[i] = 1
#         path.append(result[i])
#         perm(lev + 1)
#         path.pop()
#         used[i] = 0


# N = int(input())
# nums = list(map(int, input().split()))
# ops = list(map(int, input().split()))

# result = []
# change = {0:'+', 1:'-', 2:'*', 3:'/'}
# for i in range(4):
#     for _ in range(ops[i]):
#         result.append(change[i])

# path = []
# used = [0] * N
# calculated = []
# perm(0)
# minV = min(calculated)
# maxV = max(calculated)

# print(maxV)
# print(minV)