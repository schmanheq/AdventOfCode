# def normal(line): 
#     return 1 if line=='MAS' else 0

# def diagonal(matrix,i,j): 
#     counter = 0
#     directions = [(-1, 1), (-1, -1), (1, -1), (1, 1)] # rechts oben, links oben, links unten, rechts unten
#     for x,y in directions:
#         if (0<=j+3*y<len(matrix[i]) and 
#             0<=i+3*x<len(matrix) and 
#             matrix[i+x][j+y]=='M' and 
#             matrix[i+2*x][j+2*y]=='A' and 
#             matrix[i+3*x][j+3*y]=='S'):
#             counter+=1
#     return counter

# def vertical(matrix,i,j):
#     counter = 0
#     letters = ['M','A','S']

#     for k in range(0,3):
#         if i+k+1>=len(matrix) or matrix[i+k+1][j]!=letters[k]:
#             break
#     else:
#         counter+=1
#     for k in range(0,3):
#         if i-(k+1)<0 or matrix[i-(k+1)][j]!=letters[k]:
#             break
#     else:
#         counter+=1
#     return counter




# with open('day4/input.txt','r') as input:
#     counter = 0
#     matrix = []
#     for line in input:
#         matrix.append(line.strip())
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j]=='X':
#                 counter+=normal(matrix[i][j+1:j+4])
#                 counter+=normal(matrix[i][j-3:j][::-1])
#                 counter+=diagonal(matrix,i,j)
#                 counter+=vertical(matrix,i,j)
            
#     print(counter)
                

#task2

def diagonal(matrix):
    if matrix[1][1]=='A':
        counter = 0
        corners = [(0,0),(0,2),(2,0),(2,2)]
        for x,y in corners:
            if matrix[x][y]=='M' and matrix[abs(2-x)][abs(2-y)]=='S':
                counter+=1
            if counter>1:
                return 1
    return 0

with open('day4/input.txt','r') as input:
    counter = 0
    matrix = []
    for line in input:
        matrix.append(line.strip())
    for i in range(len(matrix)-2):
        for j in range(len(matrix[i])-2):
            matrix_to_be_checked = [matrix[i][j:j+3],matrix[i+1][j:j+3],matrix[i+2][j:j+3]]
            counter+=diagonal(matrix_to_be_checked)
    print(counter)


