# 1945. 간단한 소인수분해
t = int(input())

for tc in range(1, t+1):
    result = {2:0, 3:0, 5:0, 7:0, 11:0}  # 반복마다 리셋
    n = int(input())

    # result의 key 순회
    for i in result.keys():
        while True:
            if n % i == 0:      # 나누어 떨어지면,
                result[i] += 1  # 해당 키의 value 1 증가
                n //= i         # n에 몫 재할당
            
            else:      # 더 이상 나누어 떨어지지 않으면,
                break  # while문 종료

    print(f'#{tc}', end=' ')
    for v in result.values():  # result의 value 차례대로 출력
        print(v, end=' ')
    print()  # 개행을 위한 코드