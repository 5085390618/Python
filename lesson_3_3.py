def thesaurus(*args):
    name = {}
    for i in sorted(args):
        first_l = i[0]
        if first_l in name:
            name[first_l] += [i]
        else:
            name[first_l] = [i]
    return name
print(thesaurus("Иван", "Мария", "Пётр", "Илья",))
