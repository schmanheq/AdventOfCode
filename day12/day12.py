
# #task1
# from collections import deque,defaultdict
# matrix = []
# counter = 0
# def optimized_bfs(i,j):
#     perimeter_dict = defaultdict(int)
#     perimeter = 4
#     area = 1
#     plant = matrix[i][j]
#     perimeter_dict[(i,j)]=0
#     matrix[i][j] = '#'
#     neighbours = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
#     queue = deque([(x,y) for (x,y) in neighbours if 0<=x<len(matrix) and 0<=y<len(matrix[0]) and matrix[x][y]==plant])

#     while queue:
#         (x,y) = queue.popleft()
#         if matrix[x][y]==plant:
#             matrix[x][y]='#'
#             area+=1
#             perimeter+=4
#             perimeter_dict[(x,y)]=0
#             neighbours=[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
#             for (a,b) in neighbours:
#                 if 0<=a<len(matrix) and 0<=b<len(matrix[0]) and matrix[a][b]==plant:
#                     queue.append((a,b))
#                 if (a,b) in perimeter_dict:
#                     perimeter-=2
            
#     #print(f"{plant} has area: {area} with perimeter {perimeter}")
#     return (area,perimeter)




# with open("day12/input.txt",'r')as input:
#     for line in input:
#         line = line.strip()
#         line = list(line)
#         matrix.append(line)
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j]!='#':
#                 (area,perimeter)=optimized_bfs(i,j)
#                 counter+=area*perimeter

#     print(counter)

#task2
from collections import deque,defaultdict
matrix = []
counter = 0
def optimized_bfs(i,j):
    perimeter_dict = defaultdict(int)
    perimeter = 4
    area = 1
    plant = matrix[i][j]
    perimeter_dict[(i,j)]=0
    matrix[i][j] = '#'
    neighbours = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    queue = deque([(x,y) for (x,y) in neighbours if 0<=x<len(matrix) and 0<=y<len(matrix[0]) and matrix[x][y]==plant])

    while queue:
        (x,y) = queue.popleft()
        if matrix[x][y]==plant:
            matrix[x][y]='#'
            area+=1
            perimeter+=4
            perimeter_dict[(x,y)]=0
            neighbours=[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            site_check = [(i-1,j-1),(i-1,j),]
            for (a,b) in neighbours:
                if 0<=a<len(matrix) and 0<=b<len(matrix[0]) and matrix[a][b]==plant:
                    queue.append((a,b))
                if (a,b) in perimeter_dict:
                    perimeter-=2
            
    #print(f"{plant} has area: {area} with perimeter {perimeter}")
    return (area,perimeter)




with open("day12/input.txt",'r')as input:
    for line in input:
        line = line.strip()
        line = list(line)
        matrix.append(line)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]!='#':
                (area,perimeter)=optimized_bfs(i,j)
                counter+=area*perimeter

    print(counter)


    # c
    # c