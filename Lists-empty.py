#Creating empty lists that require user input
names=[]
marks=[]

#Using indexing to limit the number and type of data users input
for i in range (1,5):
    x=input(f"Please enter your name {i}: ")
    y= int (input(f"Please enter the marks of {x}:"))
    names.append(x)
    marks.append(y)
print(names)
print(marks)
for a,b in zip (names,marks):
    print(f"{a}:{b}")

