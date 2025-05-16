file_reader=open ("candy.txt", "r")
# print(file_reader.read())
print(file_reader.read(5))
# print(file_reader.readline(4))


for variable in file object:
print(object)

for x in file_reader:                 #method1
    print(x)

for x in range(2):                    #method2
    z=file_reader.readline
    print(z)

z=file_reader.readline()     #method 3
file_reader.close ()
file_reader=open ("candy.txt", "r")
k=file_reader.readline()
j=file_reader.readline()
print(z)
print(k)
print(j)


with open ("candy.txt", "r") as file:         #method4
    for _ in range (2):
        line=file.readline()
        if not line:
            break
        print(line,end="")



