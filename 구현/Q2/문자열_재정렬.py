N = input()
N = list(N)

char=[]
num=[str(x) for x in range(0,10)]
number=[]

for i in N:
  if i in num:
    number.append(i)
  else:
    char.append(i)

char.sort()
number= sum(int(n) for n in number)

s=char[0]
for i in char[1:]:
  s += i
s +=str(number)
print(s)

'''
2번째 풀이

data = input()
result = []
value =0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value!=0:
    result.append(str(value))

print(''.join(result))
'''