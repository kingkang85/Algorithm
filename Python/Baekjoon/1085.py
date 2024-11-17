# 1085. 직사각형에서 탈출
import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

result = min(x-0, y-0, w-x, h-y)
print(result)