def solution(today, terms, privacies):
    answer = []
    term_dic = {}
    year,month,day = map(int,today.split('.'))
    
    for term in terms:
        char, valid = term.split()
        term_dic[char] = int(valid)
    
    for i in range(len(privacies)):
        date, char = privacies[i].split()
        
        p_year,p_month,p_day = map(int,date.split('.'))
        add_date = (term_dic[char]+p_month)

        v_year = p_year + (add_date // 12) if add_date % 12 != 0 else p_year + (add_date // 13)
        v_month = add_date%12 if add_date%12 != 0 else 12
        v_day = p_day-1

        if v_day == 0:
            v_month -= 1
            if v_month == 0:
                v_year -= 1
                v_month = 12
            v_day = 28
        
        if v_year > year:
            continue
        elif v_year == year:
            if v_month > month:
                continue
            elif v_month == month:
                if v_day < day:
                    answer.append(i+1)
            else:    
                answer.append(i+1)
        else:
            answer.append(i+1)
    return answer