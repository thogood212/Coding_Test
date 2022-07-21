def possible(answer):
    for x,y, stuff in answer:
        if stuff == 0: #설치된 종류가 기둥일때
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y,-1,0] in answer:
                continue
            return False
        elif stuff ==1: # 설치된 종류가 보일때
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1]in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer=[]
    for frame in build_frame: #작업개수 최대 1000개
        x,y,stuff,operate = frame
        if operate ==0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        if operate ==1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)