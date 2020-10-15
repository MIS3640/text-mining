a = 3
a + 2
a = a + 1.0
print(a)
b = 3
print(b)
a = 3
print(a == 5.0)
print(a)
b = 10
c = b > 9
# print(c)
# print(5/2 == 5/2.0)
# print(3.0 - 1.0 != 5.0 - 3.0)
# print(3 > 4 or (2 < 3 and 9 > 10))
# print(4 > 5 or 3 < 4 and 9 > 8)
# print(not(4 > 3  and 100 > 6))
# import time
# print(time.time())
# ct= time.time()-50*365*24*60*60-1*24*60*60-28*24*60*60
# print(ct/60/60)
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370)))

import time
print(time.time())
current=time.time()
second=current % 60
minutes= (current // 60) % 60
hours = (current // 60) // 60 % 24
days = current // 60 // 60 // 24

print(
    f"current time: {int(days):d} days, {int}"
)



