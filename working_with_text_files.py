def read_all_txt(file_name):
    with open(file_name, 'r') as file:
        print(file.read())


def read_txt_by_line(file_name):
    count = 1
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(f"{count}. {line}")
            count+=1

def write_txt(file_name, str):
    with open(file_name, 'w') as file:
        file.write(str)

def append_txt(file_name, str):
    with open(file_name, 'a') as file:
        file.write(f"\n{str}")


#read_all_txt('./samples/files_to_read/backup.py')
#read_txt_by_line('./samples/files_to_read/backup.py')
#write_txt("./samples/files/example.txt", 'this is a test')
#append_txt("./samples/files/example.txt", 'Another line in the example')