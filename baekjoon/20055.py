# 20055. 컨베이어 벨트 위의 로봇
'''
먼저, 0번 칸에 로봇 visited 표시 후 -1

다음 단계 반복
1. 벨트 한 칸씩 옮기기 (visited도 같이 옮기는데..) 도착하면 내려라
2. 거꾸로 visited = 1인 것부터 이동할 수 있는 지 확인
    - visited = 0이고 내구도 1 이상인 지 확인
    - 전 위치 visited = 0으로 바꾸고 다음 위치 visited = 1
3. 0번 칸 로봇 올릴 수 있는 지 확인
4. 0인 칸 K개 이상인 지 확인
'''
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 사전 작업
visited = [0] * (2*N)
arr[0] -= 1
visited[0] = 1

cnt = arr.count(0)
while cnt < K:
    for i in range(2*N):
        i = (i+1) % (2*N)