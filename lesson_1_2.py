cube_list = [a ** 3 for a in range(1, 1000, 2)]
print(cube_list)

for i in cube_list:
    c = 0
    k = i
    while k > 0:
        u = k % 10
        k = k // 10
        c = c + u
    if c % 7 == 0:
        print(i)

increase = 17
for idx in range(len(cube_list)):
    cube_list[idx] += increase
print(cube_list)
