def solution(phone_book):
    hash_phone = dict()
    for i in phone_book:
        hash_phone[i]=1
    for j in phone_book:
        temp=''
        for k in j:
            temp+=k
            if temp != j and temp in hash_phone:
                return False
    return True
    
    