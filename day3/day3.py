# Part 1
# counter = 0
# with open('day3/input.txt','r') as input:
#     for line in input:
#         i=0
#         while i<len(line):
#             if line[i]=='m':
#                 if line[i+1:i+4]=='ul(':
#                     j = i+4
#                     num1='0'
#                     num2 = '0'
#                     while line[j].isdigit() and j<i+7:
#                         num1+=line[j]
#                         j+=1
#                     if line[j]==',':
#                         j+=1
#                         k = j+3
#                         while line[j].isdigit() and j<k:
#                             num2+=line[j]
#                             j+=1
#                         if line[j]==')':
#                             counter+=int(num1)*int(num2)  
#                     i=j             
#                 else:
#                     i+=1
#             else:
#                 i+=1
#     print(counter)

# Part 2
counter = 0
with open('day3/input.txt','r') as input:
    do_it = 1
    for line in input:
        i=0
        while i<len(line):
            if line[i]=='m':
                if line[i+1:i+4]=='ul(':
                    j = i+4
                    num1='0'
                    num2 = '0'
                    while line[j].isdigit() and j<i+7:
                        num1+=line[j]
                        j+=1
                    if line[j]==',':
                        j+=1
                        k = j+3
                        while line[j].isdigit() and j<k:
                            num2+=line[j]
                            j+=1
                        if line[j]==')':
                            counter+=(int(num1)*int(num2))*do_it 
                            if counter >= 57102097:
                                print(counter)
                            #print(counter)
                    i=j             
                else:
                    i+=1
            elif line[i]=='d':
                j = i+1
                if line[j:j+3]=="o()":
                    do_it = 1
                    j+=2
                elif line[j:j+6]=="on't()":
                    do_it = 0
                    j+=5
                i=j
                print(do_it)
            else:
                i+=1
            
    print(counter)
