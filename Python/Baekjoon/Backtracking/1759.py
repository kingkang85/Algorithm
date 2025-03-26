# 1759. 암호 만들기
import sys
input = sys.stdin.readline

def check(arr):
    v_count = c_count = 0

    for s in arr:
        if s in vowel:
            v_count += 1
        else:
            c_count += 1
        
        if v_count >= 1 and c_count >= 2:
            return True
    
    return False
    
def backtracking(arr):
    if len(arr) == L and check(arr):
        print("".join(arr))
        return
    
    for i in range(len(arr), C):
        if arr[-1] < alphabets[i]:
            arr.append(alphabets[i])
            backtracking(arr)
            arr.pop()

L, C = map(int, input().split())
alphabets = input().split()

alphabets.sort()
vowel = ['a', 'e', 'i', 'o', 'u']

for i in range(C - L + 1):
    arr = [alphabets[i]]
    backtracking(arr)
