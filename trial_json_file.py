import json
with open("data.json", "r") as file_in:
    data=json.load(file_in)
    print(data)

with open("./output.json", "w") as file_out:
    json.dump(data,file_out,indent=4)
with open("output.json", "r") as file_in1:
    data=json.load(file_in1)
    print(data)