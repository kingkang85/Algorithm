# 20551. 증가하는 사탕 수열
def Candies():
    eat = 0
    while 1:
        for i in range(2):
            if nums[i] >= nums[i+1]:  # 앞에 있는 사탕의 수가 더 크거나 같으면,
                eat += 1              # 하나 먹고
                nums[i] -= 1          # 앞 사탕 수 -1

                if nums[i] < 1:  # 먹다가 0개 되면 -1 return
                    return -1
                break  # break 후 다시 반복
            
        else:  # for문에 break 안 걸리면 while문 종료
            break
    
    return eat
    
        
T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    print(f'#{tc} {Candies()}')

############################################################################################
T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    if B < 2 or C < 3:
        print(f'#{tc} -1')
        continue

    eat = 0
    if B >= C:  # B와 C부터 비교
        eat += B - (C - 1)
        B = C - 1

    if A >= B:
        eat += A - (B - 1)
        A = B - 1

    print(f'#{tc} {eat}')