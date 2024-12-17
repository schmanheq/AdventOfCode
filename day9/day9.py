import time
data = []
convertion = ''
j = 0 

def shifting(data):
    free = 0
    last = len(data)-1
    while data[free]!='.':
        free+=1
    while data[last]=='.':
        last-=1
    while free<=last:
        data[free]=data[last]
        data[last]='.'
        while data[free]!='.':
            free+=1
        while data[last]=='.':
            last-=1
    return data

def calc_checksum(data):
    checksum = 0
    for i in range(0,len(data)):
        if data[i]=='.':
            return checksum
        checksum+=int(data[i])*i
    return checksum

with open('day9/input.txt','r')as input:
    for char in input:
        data = list(char)
    if len(data)%2==1:
        data.append('0')
    for i in range(0,len(data)-1,2):
        convertion+=(str(j))*int(data[i])
        convertion+=('.'*int(data[i+1]))
        j+=1
    convertion=list(convertion)
    convertion = shifting(convertion)
    result = calc_checksum(convertion)
    print(result)



#solution: 6408966547049