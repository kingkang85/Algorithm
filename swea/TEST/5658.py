# 5658. [모의 SW 역량테스트] 보물상자 비밀번호
# 16진수 -> 10진수로 바꾸는 함수
def hextodec(hex):
    intV = 0
    for h in hex:
        if h.isdigit():
            intV = (intV * 16) + ord(h) - ord('0') 
        else:
            intV = (intV * 16) + ord(h) - ord('A') + 10
    
    return intV
    

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lock = input()

    codes = set()  # 16진수 비밀번호들
    for i in range(N):
        code = ''
        for j in range(N//4):
            code += lock[(i+j) % N]
        codes.add(code)

    result = []
    for code in codes:
        result.append(hextodec(code))  # 10진수로 바꾼 비밀번호 추가

    result.sort(reverse=True)  # 내림차순 정렬
    print(f'#{tc} {result[K-1]}')