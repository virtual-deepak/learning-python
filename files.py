def find_acronym():
    acronym = input("Enter the acronym: ")
    try:
        with open("acronyms.txt") as file:
            lines = file.readlines()
            for line in lines:
                if (acronym in line):
                    print(f"{line}")
                    return
        print(f"Acronym {acronym} does not exist!")
    except Exception as ex:
        print(f"Exception occurred: {str(ex)}")

def add_acronym():
    acronym = input("Enter the acronym: ")
    full_form = input("Enter full form: ")
    with open("acronyms.txt", "a") as file:
        file.write(f"{acronym}: {full_form}\n")

def main():
    choice = None
    while choice != "E":
        choice = input("Do you want to find(F) or add(A) an acronym?. Press 'E' for exit..\n")
        if choice == "F":
            find_acronym()
        elif choice == "A":
            add_acronym()
        elif choice == "E":
            break;
        else:
            print('Enter a valid option!')

main()
    