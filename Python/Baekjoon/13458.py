# 13458. 시험 감독
# 정답 !!!
N = int(input())
A_i = list(map(int, input().split()))
B, C = map(int, input().split())

need = len(A_i)
for i in range(N):
    A_i[i] -= B   
    if A_i[i] > 0:  # 남은 사람이 양수일 때만 실행
        ans = A_i[i] // C
        if ans == 0:
            need += 1
        else:
            need += ans
            if A_i[i] % C != 0:
                need += 1
print(need)


##################################################################################################
# 오답 1
# N = int(input())
# A_i = list(map(int, input().split()))
# B, C = map(int, input().split())

# need = len(A_i)  # 총감독관의 수로 초기화
# for i in range(N):
#     A_i[i] -= B  # 총감독관이 관리하는 수 제외 
#     while A_i[i] > 0: 
#         A_i[i] -= C  # 부감독관이 관리하는 수 제외
#         need += 1

# print(need)


# 오답 2
# N = int(input())
# A_i = list(map(int, input().split()))
# B, C = map(int, input().split())

# need = len(A_i)
# for i in range(N):
#     A_i[i] -= B
    
#     ans = A_i[i] // C
#     if ans == 0:
#         need += 1
#     else:
#         need += ans
#         if A_i[i] % C != 0:
#             need += 1
# print(need)