from collections import defaultdict
def solution(commands):
    answer = []
    graph = [[False] * 3 for _ in range(3)]
    dic = defaultdict(list)
    merge_dic = defaultdict(list)

    for command in commands:
        print(command)
        split_command = command.split()
        if split_command[0] == 'UPDATE':
            if len(split_command) == 4:
                graph[int(split_command[1])][int(split_command[2])] = split_command[3]
                dic[split_command[3]].append([int(split_command[1]),int(split_command[2])])
            else:
                for x,y in dic[split_command[1]]:
                    graph[x][y] = split_command[2]
        elif split_command[0] == 'MERGE':
            r1,c1,r2,c2 = int(split_command[1]),int(split_command[2]),int(split_command[3]),int(split_command[4])
            
            merge_dic[(r1,c1)].append([r2,c2])
            merge_dic[(r2,c2)].append([r1,c1])

            for x,y in merge_dic[(r2,c2)]:
                merge_dic[(r1,c1)].append([x,y])
            for x,y in merge_dic[(r1,c1)]:
                merge_dic[(r2,c2)].append([x,y])
                
            if graph[r1][c1] and graph[r2][c2]:
                graph[r2][c2] = graph[r1][c1]
                for x,y in merge_dic[(r2,c2)]:
                    graph[x][y] = graph[r1][c1]
            elif not graph[r1][c1] and graph[r2][c2]:
                graph[r1][c1] = graph[r2][c2]
                for x,y in merge_dic[(r1,c1)]:
                    graph[x][y] = graph[r2][c2]
            elif graph[r1][c1] and not graph[r2][c2]:
                graph[r2][c2] = graph[r1][c1]
                for x,y in merge_dic[(r2,c2)]:
                    graph[x][y] = graph[r1][c1]
            
        elif split_command[0] == 'UNMERGE':
            
            r,c = int(split_command[1]),int(split_command[2])
            for x,y in merge_dic[(r,c)]:
                print('unmerged: ' ,x,y)
                merge_dic[(x,y)] = []
                graph[x][y] = False
        elif split_command[0] == 'PRINT':
            if not graph[int(split_command[1])][int(split_command[2])]:
                answer.append("EMPTY")
            else:
                answer.append(graph[int(split_command[1])][int(split_command[2])])
        for g in graph:
            print(g)
        print()
        print(merge_dic)
    return answer

print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))