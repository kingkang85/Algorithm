# 7682. 틱택토
'''
1. X가 이긴 경우 : X의 개수가 1개 더 많음 
2. O가 이긴 경우 : X와 O의 개수가 같음
3. 이긴 사람이 없을 경우 : X의 개수 5, O의 개수 4
'''
import sys
input = sys.stdin.readline

def check(s):
    # 가로 확인
    for i in range(0, 9, 3):
        if game[i] == game[i+1] == game[i+2] == s:
            return True
        
    # 세로 확인
    for i in range(3):
        if game[i] == game[i+3] == game[i+6] == s:
            return True
        
    # 대각선 확인
    if game[0] == game[4] == game[8] == s:
        return True
    
    if game[2] == game[4] == game[6] == s:
        return True
    
    return False

while True:
    game = input().strip()
    if game == 'end':
        break

    winX, winO = check('X'), check('O')  # 이긴 사람 확인
    cntX, cntO = game.count('X'), game.count('O')  # 각 개수 확인

    if winX and not winO and cntX == cntO + 1:
        print('valid')
    elif winO and not winX and cntO == cntX:
        print('valid')
    elif not winX and not winO and cntX == 5 and cntO == 4:
        print('valid')
    else:
        print('invalid')