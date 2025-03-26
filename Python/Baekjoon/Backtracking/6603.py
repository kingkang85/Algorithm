# 6603.로또
import sys
input = sys.stdin.readline

def dfs(dep, start, arr):
    if dep == 6:
        print(" ".join(map(str, arr)))
        return
    
    for i in range(start, k):
        arr.append(s[i])
        dfs(dep+1, i+1, arr)
        arr.pop()

while True:
    tc = list(map(int, input().split()))
    
    if tc[0] == 0:
        break
    
    k = tc[0]
    s = tc[1:]
    s.sort()

    dfs(0, 0, [])
    print()
    