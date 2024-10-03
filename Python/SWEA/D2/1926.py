# 1926. 간단한 369 게임
N = int(input())

for i in range(1, N+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        cnt = 0
        for j in str(i):
            if j in ['3', '6', '9']:
                cnt += 1
        print('-'*cnt, end=' ')

    else:
        print(i, end=' ')

####### 다른 풀이 #######
N = int(input())

for i in range(1, N+1):
    i = str(i)
    cnt = i.count('3') + i.count('6') + i.count('9')

    if cnt == 0:
        print(i, end=' ')
    else:
        print('-'*cnt, end=' ')