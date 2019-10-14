import random
import time 

list_if_time = list()
list_elif_time = list()

for i in range(10):
    if_start_time = time.time()
    for i in range(1000000):
        a = random.randint(0,15)
        if a == 1:
            a += 1
        if a == 2:
            a += 1
        if a == 3:
            a += 1
        if a == 4:
            a += 1
        if a == 5:
            a += 1
        if a == 6:
            a += 1
        if a == 7:
            a += 1    
        if a == 8:
            a += 1
        if a == 9:
            a += 1
        if a == 10:
            a += 1
        if a == 11:
            a += 1
        if a == 12:
            a += 1
        if a == 13:
            a += 1
        if a == 14:
            a += 1
        if a == 15:
            a += 1
    time_excute = time.time() - if_start_time
    print("IF TIME:\t" + str(time_excute))
    list_if_time.append(time_excute)

    elif_start_time = time.time()
    for i in range(100000):
        a = random.randint(0,15)
        if a == 1:
            a += 1
        elif a == 2:
            a += 1
        elif a == 3:
            a += 1
        elif a == 4:
            a += 1
        elif a == 5:
            a += 1
        elif a == 6:
            a += 1
        elif a == 7:
            a += 1    
        elif a == 8:
            a += 1
        elif a == 9:
            a += 1
        elif a == 10:
            a += 1
        elif a == 11:
            a += 1
        elif a == 12:
            a += 1
        elif a == 13:
            a += 1
        elif a == 14:
            a += 1
        elif a == 15:
            a += 1
    time_excute = time.time() - elif_start_time
    print("ELIF TIME:\t" + str(time_excute))
    list_elif_time.append(time_excute)

print("\n\n\n")
avg_if_time = 0
for i in list_if_time:
    avg_if_time += i
print("IF AVG TIME:\t" + str(avg_if_time/len(list_if_time)))

avg_elif_time = 0
for i in list_elif_time:
    avg_elif_time += i
print("ELIF AVG TIME:\t" + str(avg_elif_time/len(list_elif_time)))
