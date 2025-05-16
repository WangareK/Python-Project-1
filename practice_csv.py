import csv
with open("data.csv","r") as file_in:
    reader=csv.reader(file_in)
    for row in reader:
        print (row)

with open("data.csv","r") as file_in:
    reader=csv.DictReader(file_in)
    for row in reader:
        print(row['name'],row['height'])

with open ("output.csv", "w", newline="") as file_out:
    writer=csv.writer(file_out)
    writer.writerow(['name','height'])
    writer.writerow(['MaryAnn',170])

with open ("output2.csv", "w", newline="") as file_out1:
    bio=['name','height']
    writer=csv.DictWriter (file_out1, fieldnames=bio)
    writer.writeheader()
    writer.writerow({'name':'MaryAnn','height':170})