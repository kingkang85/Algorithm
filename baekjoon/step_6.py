# 6단계. 심화 1
# 25083. 새싹
print('''         ,r\'\"7
r`-_   ,\'  ,/
 \\. \". L_r\'
   `~\\/
      |
      |''')

# 3003. 킹, 퀸, 룩, 비숍, 나이트, 폰
pieces = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().split()))
need = []
for i in range(6):
    if found[i] == pieces[i]:
        need.append(0)
    else:
        need.append(pieces[i] - found[i])
for j in need:
    print(j, end=' ')

pieces = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().split()))
n = len(pieces)
for i in range(n):
    print(pieces[i]-found[i], end=' ')

# 2444. 별 찍기 - 7
n = int(input())
for i in range(1, n+1):
    print(' '*(n-i) + '*'*(2*i-1))
for j in range(n-1, 0, -1):
    print(' '*(n-j) + '*'*(2*j-1))

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

# 2941. 크로아티아 알파벳
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alphabet = input()

for i in croatia:
    alphabet = alphabet.replace(i, '*')
    
print(len(alphabet))
    
# 1316. 그룹 단어 체커
n = int(input())
cnt = n  # 그룹 단어의 수 n으로 할당

for _ in range(n):
    word = input()
    
    for i in range(len(word)-1):
        if word[i] == word[i+1]:  # 앞뒤 글자가 같다면 continue
            continue
        
        elif word[i] in word[i+2:]:  # 앞글자가 뒤에 다시 나온다면,
            cnt -= 1                 # 그룹 단어가 아니므로 -1
            break
        
print(cnt)

    
    