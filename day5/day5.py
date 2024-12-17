#task1
pairs=[]
graph={}  #SPEICHERT VORGÄNGER

# with open('day5/input.txt','r') as input1:
#     for line in input1:
#         pair = line.split('|')
#         pairs.append((pair[0],pair[1].strip()))

#     for (x,y) in pairs:
#         if y not in graph:
#             graph[y]=[]
#         graph[y].append(x)

# with open('day5/input2.txt','r') as input2:
#     counter = 0
#     for line in input2:
#         line = line.split(',')
#         line[-1] = line[-1].strip()
#         for i in range(1,len(line)):
#             if line[i-1] not in graph[line[i]]:
#                 break
#         else:
#             mid = len(line)//2
#             counter+=int(line[mid])

# print(counter)


#task2
pairs = []
graph={}  #SPEICHERT VORGÄNGER
counter = 0
task2_input = []


with open('day5/input.txt','r') as input1:
    for line in input1:
        pair = line.split('|')
        pairs.append((pair[0],pair[1].strip()))

    for (x,y) in pairs:
        if y not in graph:
            graph[y]=[]
        if x not in graph:
            graph[x]=[]
        graph[y].append(x)

with open('day5/input2.txt','r') as input2:
    counter = 0
    for line in input2:
        line = line.split(',')
        line[-1] = line[-1].strip()
        for i in range(1,len(line)):
            if line[i-1] not in graph[line[i]]:
                task2_input.append(line)
                break
print(task2_input)

for line in task2_input:
    i = 1
    while i<len(line):
        if line[i-1] not in graph[line[i]]:
            puffer = line[i-1]
            line[i-1]=line[i]
            line[i]=puffer
            if i>1:
                i-=1
        else:
            i+=1
    counter+=int(line[len(line)//2])

print(counter)     


# 97,13,75,29,47 
# 97 75 13 29 47 
# 97 75 29 13 47 
# 97 75 29 47 13 
# 97 75 47 29 13 
