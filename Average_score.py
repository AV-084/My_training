students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list (students)
print (students_list)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
a = [sum (grades[0])/len (grades[0]), sum (grades[1])/len (grades[1]), sum (grades[2])/len (grades[2]), sum (grades[3])/len (grades[3]), sum (grades[4])/len (grades[4])]
print(a)
b = set(a)
print(set(b))


zipped = zip (students_list, b)
print(zipped)
