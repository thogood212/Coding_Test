def solution(board):
    answer = 1
    list_ = [(0,0),(1,1),(2,2)]
    list_x = [(2,0),(1,1),(0,2)]
    O=0;X=0;empty=0
    Omax=0;Xmax=0
    #X는 O개수를 앞지를 수없다.
    for x in range(3):
        Ow=0;Xw=0
        for y in range(3):
            if board[x][y] =='O':
                O+=1
                Ow+=1
            elif board[x][y] =='X':
                Xw+=1
                X+=1
            else:
                empty+=1
        Omax=max(Ow,Omax)
        Xmax=max(Xw,Xmax)

    for y in range(3):
        Oh=0;Xh=0
        for x in range(3):
            if board[x][y] =='O':
                Oh+=1
            elif board[x][y] =='X':
                Xh+=1
        Omax=max(Oh,Omax)
        Xmax=max(Xh,Xmax)

    Oh=0;Xh=0
    for x,y in list_:
        if board[x][y] =='O':
            Oh+=1
        elif board[x][y] =='X':
            Xh+=1

    Omax=max(Oh,Omax)
    Xmax=max(Xh,Xmax)
    #print(Omax,Xmax)
    Oh=0;Xh=0
    for x,y in list_x:
        if board[x][y] =='O':
            Oh+=1
        elif board[x][y] =='X':
            Xh+=1
    Omax=max(Oh,Omax)
    Xmax=max(Xh,Xmax)
    

    if Omax==3 and (Xmax==3 or O==X):
        answer=0
    if empty ==0:
        if O<5 and X<4:
            answer=0

    #전체갯수가 틀린경우
    if O<X or abs(O-X)>1:
        answer = 0
    if (Omax<3 and Xmax==3) and abs(O-X)!=0:
        answer = 0

    return answer