# 2531. 회전 초밥
# import sys
# input = sys.stdin.readline

# N, d, k, c = map(int, input().split())  # N: 접시수, d: 초밥 가짓수, k: 연속 접시수, c: 쿠폰 번호
# dishes = []
# for _ in range(N):
#     dishes.append(int(input()))

# eat = dishes[:k]  # 초기 연속 접시
# types = set(eat)
# max_cnt = len(types)  # 초밥의 가짓수

# # 쿠폰 초밥
# if c not in types:
#     max_cnt += 1

# # 앞에서 빼고 뒤에 추가하며 초밥의 가짓수 갱신
# for i in range(N-1):
#     eat.pop(0)
#     eat.append(dishes[(i + k) % N])

#     types = set(eat)
#     cnt = len(types)

#     if c not in eat:
#         cnt += 1

#     max_cnt = max(max_cnt, cnt)

# print(max_cnt)

############################################################################################################
# 시간복잡도 : O(N) => 왜 틀렸지??
from collections import defaultdict
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
dishes = [int(input()) for _ in range(N)]

sushi_types = defaultdict(int)
max_cnt = 0

# 초기 윈도우 설정
for i in range(k):
    sushi_types[dishes[i]] += 1

# 쿠폰 초밥 고려
sushi_types[c] += 1

# 슬라이딩 윈도우
for i in range(N-1):
    max_cnt = max(max_cnt, len(sushi_types))

    # 이전 초밥 제거
    sushi_types[dishes[i]] -= 1
    if sushi_types[dishes[i]] == 0:
        del sushi_types[dishes[i]]

    # 새 초밥 추가
    sushi_types[dishes[(i + k) % N]] += 1

    # 쿠폰 초밥이 제거됐다면 다시 추가
    if sushi_types[c] == 0:
        sushi_types[c] += 1

print(max_cnt)