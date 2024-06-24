
file_path = 'aula10.txt'


with open(file_path, 'w+') as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.writelines(("Line 3\n", "Line 4\n"))
    
    file.seek(0, 0)
    print(file.read())
    print("Reading")
    file.seek(0, 0)
    print(file.readline(), end="")
    print(file.readline().strip())
    print(file.readline().strip())
    print()
    print("ReadLines")
    file.seek(0, 0)
    for line in file.readlines():
        print(line.strip())
    print()
        
print("#" * 10)

with open(file_path, 'r') as file:
    print(file.read())
    