# 1244. 스위치 켜고 끄기
N = int(input())
switch = input().split()
student = int(input())

for _ in range(student):
    s, num = map(int, input().split())
    start = num - 1  # 문제에서 시작 번호가 1이므로 인덱스로 사용하기 위해 -1

    # 남학생일 때
    if s == 1:
        # num칸씩 뛰어 넘으며 스위치 상태 바꾸기
        for i in range(start, N, num):
            if switch[i] == '1':
                switch[i] = '0'

            else:
                switch[i] = '1'
        
    # 여학생일 때
    else:
        for j in range(N//2):
            nj1 = start - j  # start 기준 왼쪽
            nj2 = start + j  # start 기준 오른쪽

            if 0<= nj1 and nj2 < N:  # 범위 설정
                if switch[nj1] == switch[nj2]:  # 같으면 상태 바꾸기
                    if switch[nj1] == '1':
                        switch[nj1] = switch[nj2] = '0'
                    else:
                        switch[nj1] = switch[nj2] = '1'

                else:  # 다르면 종료
                    break

for i in range(0, N, 20):
    print(*switch[i:i+20])
    