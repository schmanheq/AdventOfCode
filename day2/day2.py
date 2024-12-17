# counter = 0
# with open('day2/input.txt', 'r') as input:
#     for line in input:
#         line = line.split(' ')
#         order = 1 if int(line[0])<int(line[1]) else -1
#         for i in range(1,len(line)):
#             diff = order * (int(line[i])-int(line[i-1]))
#             if diff>3 or diff<1:
#                 break
#         else:
#             counter+=1
#     print(counter)

counter = 0
with open('day2/input.txt', 'r') as input:
    for line in input:
        line = line.split(' ')
        line = [int(x) for x in line]
        diff = line[0]-line[1]
        order = -1 if line[0]<line[1] else 1
        last_order = order
        a = True
        for i in range(2,len(line)):
            if not(0<diff*order<4) or order!=last_order:
                if a:
                    a=False
                    diff = line[i-1]-line[i]
                    order = -1 if line[i-1]<line[i] else 1
                else:
                    break
            else:
                diff = line[i-1]-line[i]
                last_order = order
                order = -1 if line[i-1]<line[i] else 1
        else:
            counter+=1
    print(counter)
        


#318

