N = str(input())
N = list(N)
num = int(len(N)/2)

left = N[:num]
right = N[num:]

a=0
b=0

for i in left:
  i = int(i)
  a += i
for j in right:
  j = int(j)
  b += j

if a==b :
  print('LUCKY')
else:
  print('READY')