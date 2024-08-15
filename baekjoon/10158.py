# 10158. 개미
import sys
# 좌표 바꿔주는 함수
def Change(c, end_c):  # 주어진 좌표 c, 격자 끝 좌표 end_c
    if ((c+t) // end_c) % 2 == 1:  # 홀수일 때
        ans = end_c - (c+t) % end_c
    
    else:  # 짝수일 때
        ans = (c+t) % end_c

    return ans

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

x = Change(p, w)
y = Change(q, h)

print(x, y)