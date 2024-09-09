# 12741. 두 전구
# 시간 초과
# 테스트 케이스가 50,000개이므로 for문에서 출력을 하면 시간 초과
T = int(input())
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())

    result = min(B, D) - max(A, C)
    if result <= 0:
        result = 0

    print(f'#{tc} {result}')

###############################################################################
# 출력이 많다면 한 번에 모아서 하자 !!
T = int(input())
result_lst = []  # 결과 저장 리스트
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())

    result = min(B, D) - max(A, C)
    if result <= 0:
        result = 0

    result_lst.append(result)

for idx, ans in enumerate(result_lst):
    print(f'#{idx + 1} {ans}')