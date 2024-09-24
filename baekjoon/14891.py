# 14891. 톱니바퀴
'''
2 6
i-1번째 행 기준
    - i-2번째 행의 2열과 i-1번째 6열 비교하여 다르면 서로 다른 방향으로 회전
    - i번째 행의 6열과 i-1번째 2열 비교
시계 방향이면 한칸씩 오른쪽
반시계면 한칸씩 왼쪽
'''

import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(4)]
K = int(input())

for _ in range(K):
    n, d = map(int, input().split())

    while True:
        arr[n-1][2]
