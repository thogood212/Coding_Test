def solution(t, p):
    answer = 0
    t_nums = []
    
    for i in range(len(t)-len(p)+1):
        j = i+len(p)
        t_num = int(t[i:j])
        print(t_num)
        if t_num<=int(p):
            t_nums.append(t_num)
    answer= len(t_nums)
    
    
    
    return answer