def num_box(num):
    for num in range(1, num + 1, 2):
        yield num
for i in num_box(15):
    print(i)
