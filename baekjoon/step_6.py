# 6단계. 심화 1
# 2444. 별 찍기 - 7
n = int(input())
for i in range(1, n+1):
    print(' '*(n-i)+'*'*(2*i-1))
for j in range(n-1, 0, -1):
    print(' '*(n-j)+'*'*(2*j-1))

# 10988. 팰린드롬인지 확인하기
word = input()
if word == word[::-1] :
    print('1')
else :
    print('0')

# 1157. 단어 공부
word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
    count = word.count(i)
    cnt.append(count)

Max = max(cnt)
if cnt.count(Max) > 1:
    print('?')
else:
    Max_index = cnt.index(Max)
    print(word_list[Max_index])