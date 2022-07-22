from itertools import permutations

def solution(n, weak, dist):
    #원형을 1자 형태로 변환
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    
    answer = len(dist)+1
    for start in range(length):
        #친구 나열하는 경우의수(순열)
        for friends in list(permutations(dist,len(dist))):
            count =1
            position = weak[start]+friends[count-1]
            # 시작점으로부터 취약 지점 확인
            for index in range(start,start+length):
                #점검 위치를 넘어가는경우
                if position<weak[index]:
                    count+=1
                    if count> len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer,count)
    if answer> len(dist):
        return -1
    return answer