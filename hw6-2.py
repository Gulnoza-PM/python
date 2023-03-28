my_list = [2, 5, 7, 3, 8, 4, 1, 9, 6]
min_val = 3
max_val = 7
indices = []
for i in range(len(my_list)):
    if my_list[i] >= min_val and my_list[i] <= max_val:
        indices.append(i)
        print(indices)