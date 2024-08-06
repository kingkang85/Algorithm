# 2605. 줄 세우기
N = int(input())
select = list(map(int, input().split()))  # 뽑은 숫자
result = [n for n in range(1, N+1)]  # N명의 학생들

for i in range(N):
    if select[i] == 0:  # 뽑은 수가 0이면 다음 학생
        continue

    else:  # 0이 아니라면
        temp = result[i]  # temp에 현재 학생 저장
        # 현재 학생이 움직이는 수만큼 하나씩 인덱스가 밀려남
        result[i-select[i]+1 : i+1] = result[i-select[i] : i]
        result[i-select[i]] = temp  # 현재 학생의 새로운 위치

print(*result)