from itertools import permutations
#왜 조합이 아닌 순열인가?

def health(k,dungeons,count):
    for i in dungeons:
        if k>=i[0] and k>=i[1]:
            k=k-i[1]
            count+=1
        else:
            continue
    return count

def solution(k, dungeons):
    answer = -1
    #피로도 k
    #피로도소모치 dungeons
    num=len(dungeons)
    combs = permutations(dungeons,num)
    max_count=0
    
    for comb in combs:
        count=0
        new = health(k,comb,count)
        max_count=max(max_count,new)
        
    return max_count