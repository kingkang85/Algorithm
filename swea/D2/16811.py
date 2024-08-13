# 16811. 당근 포장하기
def Cal(sm, mb):
    small = carrot[:sm]
    medium = carrot[sm:mb+1]
    big = carrot[mb+1:]
    c = N // 2
    if len(small) > c or len(medium) > c or len(big) > c or small[-1] == medium[0] or medium[-1] == big[0]:
        return -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))


    for sm in range(1, N-1):
        for mb in range(sm, N-1):
            print(sm, mb)

