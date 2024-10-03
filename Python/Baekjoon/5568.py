# 5568. 카드 놓기
import sys
input = sys.stdin.readline

def Choose(lev, ans):  # lev: 선택 카드 개수, ans: 만든 정수 조합
    if lev == K:
        get_num.add(ans)
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = 1
            Choose(lev + 1, ans + nums[i])
            used[i] = 0
        
        
N = int(input())
K = int(input())
nums = [input().strip() for _ in range(N)]

get_num = set()  # 만든 정수 저장 (중복 제외)
used = [0] * N
Choose(0, '')

print(len(get_num))