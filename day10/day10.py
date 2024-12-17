# #task1
# matrix = []
# counter = 0

# def search_path(i,j,current,reached):
#     if matrix[i][j]==9:
#         if (i,j) not in reached:
#             reached[(i,j)]=0
#             return 1
#         else:
#             return 0
#     path_count = 0
#     hor_directions = [j-1,j+1,]
#     ver_directions = [i-1,i+1]
#     for dir in hor_directions:
#         if 0<=dir<len(matrix[0]) and matrix[i][dir]==current+1:
#             path_count+=search_path(i,dir,current+1,reached)
        
#     for dir in ver_directions:
#         if 0<=dir<len(matrix) and matrix[dir][j]==current+1:
#             path_count+=search_path(dir,j,current+1,reached)
#     return path_count
    


# with open('day10/input.txt','r')as input:
#     for line in input:
#         line = line.strip()
#         line = list(line)
#         line = [int(x) for x in line]
#         matrix.append(line)
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j]==0:
#                 reached ={}
#                 counter+=search_path(i,j,0,reached)
# print(counter)

#task2
matrix = []
counter = 0
def search_path(i,j,current):
    if matrix[i][j]==9:
        return 1
    path_count = 0
    hor_directions = [j-1,j+1,]
    ver_directions = [i-1,i+1]
    for dir in hor_directions:
        if 0<=dir<len(matrix[0]) and matrix[i][dir]==current+1:
            path_count+=search_path(i,dir,current+1)
        
    for dir in ver_directions:
        if 0<=dir<len(matrix) and matrix[dir][j]==current+1:
            path_count+=search_path(dir,j,current+1)
    return path_count
    


with open('day10/input.txt','r')as input:
    for line in input:
        line = line.strip()
        line = list(line)
        line = [int(x) for x in line]
        matrix.append(line)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                counter+=search_path(i,j,0)
print(counter)
