# 타켓 넘버
def dfs(numbers, target, dep, midSum):
    global cnt
    if dep == len(numbers):
        if midSum == target:
            cnt += 1
        return
    
    dfs(numbers, target, dep + 1, midSum + numbers[dep])  # + 했을 때
    dfs(numbers, target, dep + 1, midSum - numbers[dep])  # - 했을 때
    
def solution(numbers, target):
    global cnt
    cnt = 0
    dfs(numbers, target, 0, 0)
    return cnt