# 10709. 기상캐스터
H, W = map(int, input().split())

for _ in range(H):
    cloud = [0] * W  # 구름 뜨는 시간
    sky = input()

    for i in range(W):
        # c인 경우에는 0 출력
        if sky[i] == 'c':
            continue
        
        # .인 경우 1 => 왼쪽에 c가 있을 때
        if 'c' in sky[:i]:
            cnt = -1  # cnt 초기 설정 주의
            for j in range(i, -1, -1):  # 왼쪽으로 가면서 c를 찾자 !
                cnt += 1
                if sky[j] == 'c':  # c를 만나면 break
                    break
            cloud[i] = cnt
                
        # .인 경우 2 => 왼쪽에 c가 없을 때
        else:
            cloud[i] = -1

    print(*cloud)