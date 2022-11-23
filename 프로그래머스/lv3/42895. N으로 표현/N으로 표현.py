def solution(N, number):
    if number == 1:
        return 1
    main_list = []
    for cnt in range(1,9):
        sub_set = set()
        sub_set.add(int(str(N)*cnt))
        for i in range(cnt-1):
            for op1 in main_list[i]:
                for op2 in main_list[-i-1]:
                    sub_set.add(op1 + op2)
                    sub_set.add(op1 * op2)
                    sub_set.add(op1 - op2)
                    if op2 != 0:
                        sub_set.add(op1 / op2)
        if number in sub_set:
            return cnt
        main_list.append(sub_set)
                
    return -1