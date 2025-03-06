import json
import os
#create a file path
file_path = '/Users/gracecostello/Desktop/student.json'

# with open(file_path, "r") as file:
    # print(file.read())

# print(os.path.exists(file_path))

#check if the file exists and works. dispay error if doesnt work
if not os.path.exists(file_path):
    print("File does not exist")

file = open(file_path, "r")
textOfFile = (file.read())

#convert string into a dictionary
json_obj = json.loads(textOfFile)

#change the name from alice to grace
json_obj["name"] = "Grace"
#write it back into the file
# with open(file_path, "w") as file:
    # file.write(str(json_obj))