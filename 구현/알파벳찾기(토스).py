from collections import Counter

def solution(s):
    answer = []
    count = 0

    s = s.lower()
    count = Counter(s).most_common()
    
    new =""

    for i in range(len(count)):
        if count[i][1]==count[0][1]:
            new += str(count[i][0])
        else:
            break
    
    new= sorted(new)
    new=''.join(sorted(new))	

    if 's' in new:
        new = new.replace('s', "")
        new = 'SS'+new

    if 'o' in new:
        new =new.replace('o', "")
        new = 'O'+new

    if 't' in new:
        new =new.replace('t', "")
        new = 'T'+new
    
    return new