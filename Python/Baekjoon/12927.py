# 12927. 배수 스위치
def Switch():
    cnt = 0  
    while 1:
        try:  # 처음으로 'Y'가 나오는 인덱스 번호 찾기
            start = bulb.index('Y')
        except:  # 'Y'가 없다면 while문 빠져나감
            break
        
        # 배수 스위치
        # 인덱스 번호는 0부터 시작하므로 배수 설정할 때 start+1
        for i in range(start, len(bulb), start+1):
            if bulb[i] == 'Y':
                bulb[i] = 'N'
            else:
                bulb[i] = 'Y'

        cnt += 1       
    return cnt
        

bulb = list(input())  # 문자열은 변경 불가하므로 리스트로 형 변환
print(Switch())