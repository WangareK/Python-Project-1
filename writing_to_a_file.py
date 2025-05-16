# #appending
file_reader=open ("candy.txt", "a")
file_reader.write("\nTrying to append")
file_reader.close()
file_reader=open ("candy.txt", "r")
z=file_reader.read()
print(z)

#rewriting
file_reader=open ("candy.txt", "w")
file_reader.write("\nTrying to rewrite")
file_reader.close()
file_reader=open ("candy.txt", "r")
z=file_reader.read()
print(z)
