old_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for i in old_list:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            new_list.append(f'"{int(i):02}"')
        else:
            new_list.append(f'"{i[0]}{int(i[1:]):02}"')
    else:
        new_list.append(i)
print(" ".join(new_list))
