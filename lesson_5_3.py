tutors = ['Иван', 'Анастасия', 'Пётр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б']

final_list = ((tutors[n], klasses[n]) if len(klasses) > n else (tutors[n], None) for n in range(len(tutors)))

print(type(final_list), *final_list, sep='\n')
