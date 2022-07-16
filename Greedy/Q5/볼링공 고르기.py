#경우의수를 파악하기
'''
1. 볼링공 무게별 개수 확인하기
2. n=전체 볼링공개수 - 무게당 볼링공수
3. 공의 개수 * 선택할 경우의수
'''
n,m= map(int,input().split())
data = list(map(int,input().split()))

array=[0]*11

for x in data:
  array[x] +=1

result=0
for i in range(1,m+1):
  n -= array[i]
  result += array[i]*n

print(result)