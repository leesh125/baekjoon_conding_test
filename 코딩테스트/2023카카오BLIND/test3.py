def permutation(arr,N):
    result = []

    if N == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in permutation(arr, N-1):
            result.append([elem] + rest)
    return result

def solution(users, emoticons):
    total = 0
    emo_plus = 0
    len_emo = len(emoticons)
    
    for perm in permutation([10,20,30,40], len_emo):
        user_total, user_emo_plus = 0,0
        for user in users:
            rate, max_price = user
            user_per_total = 0
            for i in range(len_emo):
                if rate <= perm[i]:
                    user_per_total += (emoticons[i] - int((emoticons[i] * (perm[i]/100))))
                if user_per_total >= max_price:
                    user_emo_plus += 1
                    user_per_total = 0
                    break
            
            user_total += user_per_total

        if user_emo_plus > emo_plus:
            emo_plus = user_emo_plus
            total = user_total
        elif user_emo_plus == emo_plus:
            if user_total > total:
                total = user_total
    
    return [emo_plus, total]

#print((1300*0.6 + 1500*0.6 + 1600*0.8+ 4900 * 0.6))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))