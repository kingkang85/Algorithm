# 21608. 상어 초등학교
N = int(input())
room = [[0] * N for _ in range(N)]
wish = [list(map(int, input().split())) for _ in range(N*N)]
sorted_wish = sorted(wish)  # 학생 번호를 기준으로 정렬 (만족도 검사 편하게)

# 자리 배정
for lst in wish:
    like_mx = empty_mx = -1
    for i in range(N):
        for j in range(N):
            if room[i][j] > 0:  # 빈 자리가 아니면 다음!
                    continue
            
            like = empty = 0  # like: 좋아하는 친구 수, empty: 빈 자리 수
            for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                ni, nj = i + di, j + dj

                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue
                
                if room[ni][nj] in lst:  # 주변에 좋아하는 친구 있으면 cnt 1 증가
                    like += 1

                if room[ni][nj] == 0:  # 주변에 빈 자리가 있으면 empty 1 증가
                    empty += 1

            # 좋아하는 친구가 더 많거나 빈 자리가 더 많으면 최댓값 갱신
            if like_mx < like or like_mx == like and empty_mx < empty:
                like_mx, empty_mx = like, empty  
                ei, ej = i, j

    room[ei][ej] = lst[0]  # 모든 위치 체크 후 최종 자리에 학생 배정                  
                     
            
# 만족도 검사
score = [0, 1, 10, 100, 1000]  # 맨 앞의 0은 무의미, 인덱스 번호대로 만족도 점수
total = 0
for i in range(N):
    for j in range(N):
        cnt = 0  # 주변 좋아하는 친구 수
        for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            ni, nj = i + di, j + dj

            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            
            # 주변 친구가 위시리스트에 있으면 cnt 1 증가
            if room[ni][nj] in sorted_wish[room[i][j] - 1]:
                cnt += 1
        
        total += score[cnt]

print(total)