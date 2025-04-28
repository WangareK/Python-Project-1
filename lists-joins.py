list1=["MaryAnn","Jane","Kevin"]
list2=["Ian","Kevin","Kyalo"]
list3=list1+list2
print(list3)
list1 +=list2
print (list1)
list1=list1+list2
print(list1)
# for item in list2:
#     list1.append(item)
# print(list1)
for x in list2:
    list1.append(x)
print(list1)
# Create three lists: graphic design, data science, students
data_science=["MaryAnn","John","Susie"]
graphic_design=["Lynn","May","Ian"]
students=graphic_design+data_science
print (students)
backup=data_science.copy()
data_science.clear()
print(data_science)
print(backup)
