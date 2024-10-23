# 1253. 좋다
import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))  # 정렬!!

cnt = 0
for i in range(N):
    target = nums[i]
    tmp = nums[:i] + nums[i+1:]  # 목표값을 제외한 수들
    
    start = 0
    end = N - 2
    while start < end:
        sumV = tmp[start] + tmp[end]
        # 두 수의 합이 target보다 크다면,
        # 더 작은 수를 만들기 위해 end를 한 칸 앞으로 이동
        if sumV > target:
            end -= 1
        # 두 수의 합이 target보다 작다면, start를 한 칸 뒤로 이동
        elif sumV < target:
            start += 1
        else:
            cnt += 1
            break

print(cnt)