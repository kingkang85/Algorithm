# 2527. 직사각형
def DeterSq():
    # 점으로 겹치는 경우
    if (x1, y1) == (p2, q2) or (p1, y1) == (x2, q2) or (p1, q1) == (x2, y2) or (x1, q1) == (p2, y2):
        return 'c'
    
    # 분리된 경우
    elif p1 < x2 or q1 < y2 or x1 > p2 or y1 > q2:
        return 'd'
    
    # 선분으로 겹치는 경우
    elif ((x1 == p2 or p1 == x2) and (not(y2 >= q1) and not(y1 >= q2))) or \
         ((y1 == q2 or q1 == y2) and (not(p2 <= x1) and not(q1 <= x2))):
        return 'b'

    # 직사각형으로 겹치는 경우
    return 'a'


for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = list(map(int, input().split()))
    Max = max(y1, q1, y2, q2)
    Min = min(y1, q1, y2, q2)
    print(DeterSq())
