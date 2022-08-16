def solution(priorities, location):
    answer = 0
    final = []
    special = max(priorities)
    while len(priorities)>0:
        if special in priorities:
            p = priorities.pop(0)
            print(p)
            location -=1
            if p == special:
                final.append(p)
                if location == -1:
                    answer = len(final)
                    print('work')
                    break
            else:
                priorities.append(p)
                if location == -1:
                    location=len(priorities)-1
            
        else:
            special -=1
    return answer