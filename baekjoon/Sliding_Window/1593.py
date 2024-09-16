# 1593. 문자 해독
# 정답 코드 (슬라이딩 윈도우 이용)
import sys
input = sys.stdin.readline

g, s = map(int, input().split())
W = input().strip()
S = input().strip()

wa = [0] * 58  # 문자열 W에서 각 문자가 몇 번 나오는지 저장
sa = [0] * 58  # 문자열 S에서 각 문자가 몇 번 나오는지 저장

# 아스키 코드를 이용하여 wa에 빈도 수 저장
for c in W:
    wa[ord(c) - ord('A')] += 1

# sa에 빈도 수 저장
start = length = cnt = 0
for c in S:
    sa[ord(c) - ord('A')] += 1
    length += 1

    # W의 길이가 되면 wa와 sa가 같은지 확인
    if length == g:
        if wa == sa:
            cnt += 1

        # 다음 구간으로 넘어가자!
        sa[ord(S[start]) - ord('A')] -= 1  # 맨 앞 글자 제거
        start += 1
        length -= 1

print(cnt)

##############################################################################################
# 오답 코드 1 (순열 이용) => 런타임 에러 (RecursionError)
# import sys
# input = sys.stdin.readline

# def perm(lev):
#     global cnt
#     if lev == Wl:
#         check = ''.join(result)

#         if check in S:
#             cnt += 1
#         return
    
#     for i in range(Wl):
#         if not used[i]:
#             used[i] = 1
#             result.append(W[i])
#             perm(lev + 1)
#             result.pop()
#             used[i] = 0

# Wl, Sl = map(int, input().split())
# W = input()
# S = input()

# cnt = 0
# result = []
# used = [0] * Wl
# perm(0)

# print(cnt)

##############################################################################################
# 오답 코드 2 (순열 모듈 이용) => 시간 초과
# from itertools import permutations
# import sys
# input = sys.stdin.readline

# Wl, Sl = map(int, input().split())
# W = input().strip()
# S = input().strip()

# cnt = 0
# for p in permutations(W):
#     check = ''.join(p)

#     if check in S:
#         cnt += 1

# print(cnt)