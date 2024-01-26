import os

cwd = r"C:\Users\sony\Desktop\Newfolder"
list = os.listdir(cwd)

file_no = 1

for file in list:
    old_path = cwd + "\\" + file
    new_path = cwd + "\\" + "File" + str(file_no) + ".txt"
    file_no = file_no + 1
    os.rename(old_path, new_path)