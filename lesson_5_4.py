box = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

final_box = [box[num] for num in range(1, len(box)) if box[num] > box[num - 1]]

print(final_box)
