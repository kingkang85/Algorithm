# 5373. 큐빙
import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    # 윗면
    top = [
        ['w', 'w', 'w'],
        ['w', 'w', 'w'],
        ['w', 'w', 'w']
   ]
    bottom =[
        ['y', 'y', 'y'],
        ['y', 'y', 'y'],
        ['y', 'y', 'y']
    ]
    front = [
        ['r', 'r', 'r'],
        ['r', 'r', 'r'],
        ['r', 'r', 'r']
    ]
    back = [
        ['o', 'o', 'o'],
        ['o', 'o', 'o'],
        ['o', 'o', 'o']
    ]
    left = [
        ['g', 'g', 'g'],
        ['g', 'g', 'g'],
        ['g', 'g', 'g']
    ]
    right = [
        ['b', 'b', 'b'],
        ['b', 'b', 'b'],
        ['b', 'b', 'b']
    ]
