# 2383. [모의 SW 역량테스트] 점심 식사시간
# 어디 계단으로 갈 지 나누는 함수
def get_comb(i, s1, s2):
    if i == P:
        get_time(s1, s2)  # 두 그룹으로 나눴으면 시간 구하러 가자!
        return

    # i번째 사람을 계단 1로
    s1.append(people[i])
    get_comb(i + 1, s1, s2)
    s1.pop()

    # i번째 사람을 계단 2로
    s2.append(people[i])
    get_comb(i + 1, s1, s2)
    s2.pop()

# 해당 계단에서 소요되는 시간 계산하는 함수
def cal_stairs_time(group, stair_info):
    sr, sc, st = stair_info  # 계단 위치 행, 열, 시간
    coming_queue = []  # 계단까지 오는 사람들
    descending_queue = []  # 계단 내려가는 사람들
    waiting_queue = []  # 계단 입구 도착 후 기다리는 사람들

    # 해당 계단까지 오는 사람들의 소요 시간 추가
    for ppl in group:
        ans = abs(ppl[0] - sr) + abs(ppl[1] - sc)
        coming_queue.append(ans)

    coming_queue.sort()  # 도착한 순서대로 정렬

    time = 0
    # 셋 중에 하나라도 사람이 남아있으면 계속 진행
    while coming_queue or descending_queue or waiting_queue:
        # 계단 내려가는 사람들 처리
        descending_queue = [t - 1 for t in descending_queue if t - 1 > 0]

        # 계단 도착한 사람들 처리
        while waiting_queue and len(descending_queue) < 3:
            descending_queue.append(st)  # 계단 내려가기 시작
            waiting_queue.pop(0)

        # 계단까지 오는 사람들 시간 - 1
        i = 0
        while i < len(coming_queue):
            if coming_queue[i] == 0:  # 도착했으면 waiting_queue에 추가
                waiting_queue.append(coming_queue.pop(i))
            else:
                coming_queue[i] -= 1
                i += 1

        # (주의) 만약 조건 설정 안 하면, 마지막에 모든 원소들이 없을 때도 1분 더 세어짐
        if coming_queue or descending_queue or waiting_queue:
            time += 1

    return time

# 총 시간 계산하는 함수
def get_time(s1, s2):
    global minV

    stair1_time = cal_stairs_time(s1, stairs[0])  # 계단 1에서 시간 계산
    stair2_time = cal_stairs_time(s2, stairs[1])  # 계단 2에서 시간 계산

    total = max(stair1_time, stair2_time)  # 둘 중에 큰 값이 총 시간
    minV = min(minV, total)  # 최소 비교


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    people = []  # 사람 위치
    stairs = []  # 계단 위치 (계단 길이도 함께 저장)

    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                people.append((i, j))

            elif room[i][j] > 1:
                stairs.append((i, j, room[i][j]))

    P = len(people)  # 사람 수
    minV = 10e5
    get_comb(0, [], [])

    print(f'#{tc} {minV}')