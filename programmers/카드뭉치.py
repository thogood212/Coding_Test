from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    q = deque(goal)
    q1 = deque(cards1)
    q2 = deque(cards2)
    b,c = q1.popleft(),q2.popleft()
    while q:
        a = q.popleft()
        if a == b:
            if len(q1) > 0:
                b = q1.popleft()
        elif a == c:
            if len(q2) > 0:
                c = q2.popleft()

        elif a != b and a!=c:
            return "No"

    return "Yes"