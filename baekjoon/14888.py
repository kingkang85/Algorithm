# 14888. 연산자 끼워넣기
def ChangeOps():
    result = []
    result.append(['+'] * ops[0])
    result.append(['-'] * ops[1])
    result.append(['*'] * ops[2])
    result.append(['//'] * ops[3])

    return result

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
print(ChangeOps())