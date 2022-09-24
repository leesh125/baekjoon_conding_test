def getMaxIdx(end_idx,arr):
    idx = 0
    for i in range(end_idx-1, -1, -1):
        if arr[i] != 0:
            idx = i
            break
    else:
        return -1
    return idx+1

def delivery(truck,arr,idx):
    for i in range(idx-1,-1,-1):
        if arr[i] != 0:
            if truck - arr[i] >= 0:
                truck -= arr[i]
                arr[i] = 0
            else:
                arr[i] -= truck
                return i+1
    return 0
                

def solution(cap, n, deliveries, pickups):
    len_deli = len(deliveries)
    len_pickups = len(pickups)
    total_dist = 0
    delIdxEnd = len_deli
    picIdxEnd = len_pickups

    while True:
        delIdx = getMaxIdx(delIdxEnd,deliveries)
        picIdx = getMaxIdx(picIdxEnd,pickups)
        if delIdx == -1 and picIdx == -1:
            return total_dist*2

        total_dist += max(delIdx,picIdx)

        delIdxEnd = delivery(cap,deliveries,delIdx)
        picIdxEnd = delivery(cap,pickups,picIdx)
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))