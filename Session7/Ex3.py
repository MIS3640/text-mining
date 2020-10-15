# current_sum = 0

# for i in range(1, 1001):
#     current_sum= current_sum + i

# print(current_sum)

# current_sum = 0

# for i in range (0, 1001, 2):
#     print(current_sum)
#     current_sum = current_sum + i
#     print(current_sum)


# iteration = 0
# while iteration < 5: 
#     count = 0
#     for letter in "hello, world": 
#         count += 1
#     print("Iteration" + str(iteration) + "; count is:" + str(count))
#     iteration += 1

# while True: 
#     line = input('> ')
#     if line == "done': 
#         break
#     print(line)

# print('Done!')

import pandas as pd
from pandas import DataFrame

# print ('pandas version: ' + pd.__version__)

d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(d)

# df = DataFrame(data = d)
# print(df)

def mysqrt(a, x): 
    while True: 
        print(x)
        y = (x + a/x) / 2
        if y == x: 
            break
        x = y           


df = DataFrame(data=d, columns=["a"])


import math

a = range(10)
x = 4
df["mysqrt(a)"] = mysqrt(a, x)
df["diff"] = abs(df["a"] - df["mysqrt(a)"])

print(df)



# product = 0
# for x in range(1, 11):
#     for y in range(1, 11): 
#         product = x * y
#         print('{:<4}'.format(product), end='')
#     print()

# row_format ="{:>15}" * (len(teams_list) + 1)
# print(row_format.format("", *teams_list))
# for team, row in zip(teams_list, data):
#     print(row_format.format(team, *row))

df = df

print(f'Centre Aligned:')
print(f'{dp:^10}|{dp:^10}|')

