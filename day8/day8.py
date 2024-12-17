# #task 1
# counter = 0 
# positions = {}
# matrix = []
# dup_antino_antenna = {}
# def calc_antinodes_locations(curr,neighbours):
#     antinodes_locations = []
#     for (x,y) in neighbours:
#         antinodes_locations.append((curr[0]+(curr[0]-x),curr[1]+(curr[1]-y)))
#         antinodes_locations.append((x+(x-curr[0]),y+(y-curr[1])))
#     return antinodes_locations

# with open('day8/input.txt','r') as input:
#     for line in input:
#         matrix.append(list(line.strip()))

#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j]!='.' and matrix[i][j]!='#':
#                 if matrix[i][j] not in positions:
#                     positions[matrix[i][j]]=[(i,j)]
#                 else:                    
#                     antinodes = calc_antinodes_locations((i,j),positions[matrix[i][j]])
#                     for (x,y) in antinodes:
#                         if 0<=x<len(matrix) and 0<=y<len(matrix[i]) and matrix[x][y]!='#':
#                             if matrix[x][y]=='.':
#                                 matrix[x][y]='#'
#                                 counter+=1
#                             else:
#                                 if (x,y) not in dup_antino_antenna:
#                                     dup_antino_antenna[(x,y)]=0
#                                     counter+=1
#                     positions[matrix[i][j]].append((i,j))
#     print(counter)

# with open('day8/new_matrix.txt','w') as file:
#     for row in matrix:
#         file.write("".join(row) + "\n")

#task 2
counter = 0 
positions = {}
matrix = []
dup_antino_antenna = {}
test = 0
def calc_antinodes_locations(curr,neighbours):
    antinodes_locations = []
    for (x,y) in neighbours: 
        i=1
        j=1
        x_1 = curr[0]+i*(curr[0]-x)
        y_1 = curr[1]+i*(curr[1]-y)
        x_2 = x+j*(x-curr[0])
        y_2 = y+j*(y-curr[1])
        while 0<=x_1<len(matrix) and 0<=y_1<len(matrix[0]):
            antinodes_locations.append((x_1,y_1))
            i+=1
            x_1 = curr[0]+i*(curr[0]-x)
            y_1 = curr[1]+i*(curr[1]-y)
        while 0<=x_2<len(matrix) and 0<=y_2<len(matrix[0]):
            antinodes_locations.append((x_2,y_2))
            j+=1
            x_2 = curr[0]+j*(x-curr[0])
            y_2 = curr[1]+j*(y-curr[1])
    return antinodes_locations

with open('day8/input.txt','r') as input:
    for line in input:
        matrix.append(list(line.strip()))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]!='.' and matrix[i][j]!='#':
                if matrix[i][j] not in positions:
                    positions[matrix[i][j]]=[(i,j)]
                else:                    
                    antinodes = calc_antinodes_locations((i,j),positions[matrix[i][j]])
                    for (x,y) in antinodes:
                        if matrix[x][y]!='#':
                            if matrix[x][y]=='.':
                                matrix[x][y]='#'
                                counter+=1
                    positions[matrix[i][j]].append((i,j))
    for key in positions.keys():
        counter+=len(positions[key])
    print(counter)

with open('day8/new_matrix.txt','w') as file:
    for row in matrix:
        file.write("".join(row) + "\n")
