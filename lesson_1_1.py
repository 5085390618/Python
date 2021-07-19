a = input('duration = ')
a = int(a)
d = a // 86400
h = (a % 86400) // 3600
m = (a - d * 86400 - h * 3600) // 60
s = a % 60
if a < 60:
    print(s, 'sec')
if 60 <= a < 3600:
    print(m, 'min ', s, 'sec')
if 3600 <= a < 86400:
    print(h, 'hor', m, 'min ', s, 'sec')
if a >= 86400:
    print(d, 'day', h, 'hor', m, 'min ', s, 'sec')
