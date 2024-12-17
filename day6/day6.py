# # Task 1
# matrix = []
# counter = 0
# directions = ['^','>','v','<']
# curr_d = 0
# def step_forward(direction,i,j):
#     if direction=='^':
#         return (i-1,j)
#     if direction=='>':
#         return (i,j+1)
#     if direction=='<':
#         return (i,j-1)
#     else:
#         return (i+1,j)

# with open('day6/input.txt','r') as input:
#     for line in input:        
#         matrix.append(list(line.strip()))


# #determining the guards starting position
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j]=='^':
#             guard = (i,j)
#             break

# while 1:
#     next_position = step_forward(matrix[guard[0]][guard[1]],guard[0],guard[1])
#     if next_position[0]<len(matrix) and next_position[1]<len(matrix[0]):
#         if matrix[next_position[0]][next_position[1]]=='.':
#             matrix[guard[0]][guard[1]]='X'
#             counter+=1
#             matrix[next_position[0]][next_position[1]]=directions[curr_d%4]
#             guard=(next_position[0],next_position[1])
#         elif matrix[next_position[0]][next_position[1]]=='#':
#             curr_d+=1
#             matrix[guard[0]][guard[1]]=directions[curr_d%4]
#         else:
#             matrix[next_position[0]][next_position[1]]=directions[curr_d%4]
#             guard=(next_position[0],next_position[1])
#     else:
#         print(counter+1)
#         break
    
# with open("day6/theGuardsWalk.txt", "w") as f:
#     for row in matrix:
#         f.write("".join(row) + "\n")

# Task 2
matrix = []
counter = 0
directions = ['^','>','v','<']
curr_d = 0
def step_forward(direction,i,j):
    if direction=='^':
        return (i-1,j)
    if direction=='>':
        return (i,j+1)
    if direction=='<':
        return (i,j-1)
    else:
        return (i+1,j)

with open('day6/input.txt','r') as input:
    for line in input:        
        matrix.append(list(line.strip()))


#determining the guards starting position
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]=='^':
            guard = (i,j)
            break

while 1:
    next_position = step_forward(matrix[guard[0]][guard[1]],guard[0],guard[1])
    if next_position[0]<len(matrix) and next_position[1]<len(matrix[0]):
        if matrix[next_position[0]][next_position[1]]=='.':
            matrix[guard[0]][guard[1]]='X'
            counter+=1
            matrix[next_position[0]][next_position[1]]=directions[curr_d%4]
            guard=(next_position[0],next_position[1])
        elif matrix[next_position[0]][next_position[1]]=='#':
            curr_d+=1
            matrix[guard[0]][guard[1]]=directions[curr_d%4]
        else:
            matrix[next_position[0]][next_position[1]]=directions[curr_d%4]
            matrix[guard[0]][guard[1]]='X'
            guard=(next_position[0],next_position[1])
    else:
        print(counter+1)
        break
    
with open("day6/theGuardsWalk.txt", "w") as f:
    for row in matrix:
        f.write("".join(row) + "\n")
