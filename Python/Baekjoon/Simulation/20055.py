# 20055. 컨베이어 벨트 위의 로봇
'''
다음 단계 반복
1. 벨트 한 칸씩 옮기기
    - 로봇도 함께 옮기기
    - 로봇이 N-1에 도착하면 제외
2. 거꾸로 visited = 1인 것부터 이동할 수 있는지 확인
    - visited = 0이고 내구도 1 이상인지 확인
    - visited = 1 설정하고 이전 위치 visited = 0
    - 로봇이 N-1에 도착하면 제외
3. 0번 칸 로봇 올릴 수 있는지 확인
4. 0인 칸 K개 이상인지 확인
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))  # 컨베이어 벨트
visited = [0] * N  # 로봇 위치
cnt = 0  # 단계 수

while True:
    cnt += 1
    
    # 벨트와 로봇 위치 한 칸씩 옮기기
    arr = [arr[-1]] + arr[:-1]
    visited = [visited[-1]] + visited[:-1]
    visited[-1] = 0  # 마지막 로봇 내리기

    # 로봇 이동시키기
    for i in range(N-2, -1, -1):
        if visited[i] == 1 and visited[i+1] == 0 and arr[i+1] >= 1:
            arr[i+1] -= 1
            visited[i+1] = 1
            visited[i] = 0  # 이전 위치는 0
    visited[-1] = 0  # 마지막 로봇 내리기
    
    # 시작 위치에 로봇 올리기
    if arr[0] != 0:
        arr[0] -=1
        visited[0] = 1
    
    # 내구도가 0인 칸의 개수가 K개 이상이면 종료
    if arr.count(0) >= K:
        break

print(cnt)