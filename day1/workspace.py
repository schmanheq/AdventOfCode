'''
Task1

list1 = []
list2 = []
counter = 0
with open('input.txt','r') as input:
    for line in input:
        line = line.strip().split(' ')
        list1.append(line[0])
        list2.append(line[-1])
    list1 = sorted(list1)
    list2 = sorted(list2)
    for i in range(len(list1)):
        counter +=abs(int(list1[i])-int(list2[i]))
    print(counter)
'''


list1 = []
list2 = []
counter = 0
with open('input.txt','r') as input:
    for line in input:
        line = line.strip().split(' ')
        list1.append(line[0])
        list2.append(line[-1])
    for i in range(len(list1)):
        counter+=int(list1[i])*(list2.count(list1[i]))
    print(counter)