# 1288. 새로운 불면증 치료법
t = int(input())
for i in range(1, t+1):
    n = int(input())
    ans = set()  # 중복을 제거하기 위한 set 자료형
    
    cnt = 1
    while True:
        for j in str(n*cnt):  # n*cnt를 문자열로 형 변환 후
            ans.add(j)        # 순회하며 ans에 추가
        cnt += 1            
        if len(ans) == 10:
            break  # ans의 요소가 0~9, 즉 10개가 되면 while문 종료
        # cnt += 1
    
    print(f'#{i} {n*cnt}')
 

####### 다른 풀이 #######
t = int(input())
for i in range(1, t+1):
    n = int(input())
    cnt = [0] * 10

    value = '0'
    while 0 in cnt:
        value = str(int(value) + n)
        for c in value:
            cnt[int(c)] += 1
    
    print(f'#{t} {value}')