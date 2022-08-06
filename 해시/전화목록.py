def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:#12,123
        hash_map[phone_number] = 1#hash_map[12]=1 {'12':1}
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:#1,2,3
            temp += number#temp='12'
            if temp in hash_map and temp != phone_number:
                answer = False
    print(temp)
    print(hash_map)
    return answer