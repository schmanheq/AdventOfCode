#task 1
# def blinking(stones):
#     i=0
#     while i<len(stones):
#         if stones[i]==0:
#             stones[i]=1
#         elif len(str(stones[i]))%2==0:
#             mid = len(str(stones[i]))//2
#             puffer = (str(stones[i])[:mid], str(stones[i])[mid:])
#             new_stones = [int(puffer[0]),int(puffer[1])]
#             if i<len(stones)-1:
#                 stones = stones[:i]+new_stones+stones[i+1:]
#             else:
#                 stones = stones[:i]+new_stones
#             i+=1
#         else:
#             stones[i]=stones[i]*2024
#         i+=1
#     return stones
# with open('day11/input.txt','r') as input:
#     for line in input:
#         start = line.split(' ')
#         start = [int(x) for x in start]
#     for i in range(25):
#         start = blinking(start)
#     print(len(start))
    

from collections import defaultdict

def lanternfish(initial_stones,iterations):
    counter = 0
    stones_timers = defaultdict(int)

    for stone in initial_stones:
        stones_timers[stone]+=1
    
    for _ in range(iterations):
        stones = dict(stones_timers)
        for stone,count in stones.items():
            if count == 0:
                pass
            elif stone==0:
                stones_timers[1]+=count
                stones_timers[0]-=count
            elif len(str(stone))%2==0:
                str_stone = str(stone)
                mid = len(str_stone)//2
                stone_1 = int(str_stone[:mid])
                stone_2 = int(str_stone[mid:])
                stones_timers[stone_1]+=count
                stones_timers[stone_2]+=count
                stones_timers[stone]-=count
            else:
                stones_timers[stone*2024]+=count
                stones_timers[stone]-=count
    for stone,count in stones_timers.items():
        counter+=count
    print(counter)    
    return 




with open('day11/input.txt','r') as input:
    for line in input:
        start = line.split(' ')
        start = [int(x) for x in start]
        lanternfish(start,75)
    
