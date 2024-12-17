# #task1
# def brute_force(line):
#     res = line[0]
#     nums = line[1:]
#     org_nums = nums
#     len_nums_org = len(nums)-1
#     i=0
#     while i<2**(len(nums)-1):
#         nums = org_nums[:]
#         binary = bin(i)
#         replace = binary[2:]
#         complete = ('0'*(len_nums_org-len(replace)))+replace
#         convert = complete.replace('0','+')
#         convert = convert.replace('1','*')
#         equation = int(nums[0])
#         for j in range(0,len(convert)):
#             if convert[j]=='*':
#                 equation= equation*int(nums[j+1])
#             else:
#                 equation+=int(nums[j+1])
#         if equation==int(res):
#             return True
#         i+=1
#     return False

# brute_force(['292', '11', '6', '16', '20'])


# counter = 0
# with open('day7/input.txt','r')as input:
#     for line in input:
#         line = line.split(' ')
#         line[-1]=line[-1].strip()
#         line[0]=line[0][:-1]
#         print(line)
#         if brute_force(line):
#             counter+=int(line[0])
# print(counter)


#task2 
from itertools import product

def brute_force(line):
    res = line[0]
    nums = line[1:]
    i=0
    while i<2**(len(nums)-1):
        binary = bin(i)
        replace = binary[2:]
        complete = ('0'*(len(nums)-1-len(replace)))+replace
        convert = complete.replace('0','+')
        convert = convert.replace('1','*')
        equation = int(nums[0])
        for j in range(0,len(convert)):
            if convert[j]=='*':
                equation= equation*int(nums[j+1])
            else:
                equation+=int(nums[j+1])
        if equation==int(res):
            return True
        i+=1
    return False

def brute_force2(line):
    combinations = list(product(['+','*','||'],repeat=len(line)-2))
    nums = line[1:]
    for combi in combinations:
        equation = nums[0]
        for i in range(0,len(nums)-1):
            if combi[i]=='+':
                equation = int(equation)+int(nums[i+1])
            elif combi[i]=='*':
                equation = int(equation)*int(nums[i+1])
            else:
                equation = str(equation)+nums[i+1]
        if int(equation)==int(line[0]):
            return True
    return False


counter = 0
with open('day7/input.txt','r')as input:
    for line in input:
        line = line.split(' ')
        line[-1]=line[-1].strip()
        line[0]=line[0][:-1]
        if brute_force(line):
            counter+=int(line[0])
        elif brute_force2(line):
            counter+=int(line[0])
print(counter)