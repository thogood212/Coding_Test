def solution(record):
    answer = []
    input=record
    dict = {}
    
    for i in input:
        i=i.split()
        if i[0] == "Enter":
            dict[i[1]]=i[2]
        elif i[0] == "Leave":
            continue
        else:
            dict[i[1]]=i[2]
    
    for i in input:
        i=i.split()
        if i[0] == "Enter":
            answer.append(f"{dict[i[1]]}님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(f"{dict[i[1]]}님이 나갔습니다.")
        else:
            continue
    
    return answer