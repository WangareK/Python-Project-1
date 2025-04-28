students=["MaryAnn","Kevin","Kyalo","Ian"]
print(students)
print("accessing list items using positive indexes")
print(students[0])
print(students[2])
print("accessing list items using negative indexing")
print(students[-1])
print(students[1:3])
print(students[:3])
print(students[1:])
print(students[-3:-1])
students[0]="Wangare"
print(students[0])
# for item in list:
#     print(item)
for k in students:
    print("Student name:",k)
# if item in list:
#     print("Yes, grade student")
if "Kobe" in students:
    print("Student to be graded")
else:
    print("Student not found")
print(len(students))
students.append("John")
print(students)
students.append("Vundi")
students.append("Brian")
print(len(students))
students.append("Ian")
print(students)
# list.insert(position,item)
students.insert(2,"Wanderi")
print(students)
# list.remove(item)
students.remove("Ian")
print(students)
# list.pop()
students.pop()
print(students)
students.pop(0)
print(students)
# list.clear  will empty the list
# students.clear()
print(students)
# del item    removes the specified index or del  list     deletes entire list
del students [0]
print(students)
# list.copy
students2=students.copy()
print(students2)
# list(old list name)
students3=list(students2)
print(students3)
students3.append("Kabogo")
print(students3)
students3.insert(2,"Kevin")
print(students3)





