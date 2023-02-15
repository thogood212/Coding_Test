#리스트에서 인덱싱 중에 인덱스가 넘어가는 경우에는 %을 사용해서 대응할것

def solution(s, skip, index):
    answer = ''
    skip_list =[]
    letters = []
    letter=''
    for i in range(len(skip)):
        skip_list.append(skip[i])
    for i in range(ord('a'),ord('z')+1):
        if chr(i) in skip_list:
            pass
        else:
            letters.append(chr(i))
    
    for i in range(len(s)):
        i = s[i]
        letter += letters[(letters.index(i)+index)%len(letters)]
    answer = letter
        
    return answer