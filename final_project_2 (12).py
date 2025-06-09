def get_number(item_name):
    while True:
        user_input = input("Please enter " + item_name + ": ")
        if not user_input.isdigit():
            print("Error: " + item_name + " Must be a number, try again")
        else:
            return int(user_input)
def id_exist(people_dict, ID):
    return ID in people_dict

def save_entry(people_dict,avgList):
    while True:
        ID =  get_number("ID")

        if id_exist(people_dict,ID):
            print("This ID already exists. Entry not saved.")
            continue
        elif  ID < 0:
            print("ID must be a positive number.")
            continue
        name = input("Name: ")
        age = input("Age: ")
        age = int(age)
        if age < 0:
            print("Age must be a non-negative number.")
            continue
        people_dict[ID] = {
            "name": name,
            "age": age
        }
        avgList[0] += age
        avgList[1] += 1
        print("ID ["+ str(ID) + "]Entry saved."   )
        break


def search_by_id(people_dict):

    ID = get_number("the ID you want to look for ")


    if int(ID) in people_dict:
        print(f"ID: {ID}")
        print(f"Name: {people_dict[ID]['name']}")
        print(f"Age: {people_dict[ID]['age']}")
    else:
        print("not exist")

def print_avg_age(avgList):
   if avgList[1] == 0:
       print("No entries")
   else:
       avg = avgList[0] / avgList[1]
       print(f"Average age: {avg}")


def print_all_names(people_dict):
    for index, ID in enumerate(people_dict):
        print(f" {index}. {people_dict[ID]['name']}")

def print_all_ids(people_dict):
    for index, ID in enumerate(people_dict.keys()):
        print(f"{index}. {ID}")

def print_all_entries(people_dict):
    for index,(ID, person) in enumerate(people_dict.items()):
        print(f"{index}, {ID}")
        print(f"   Name: {person['name']}")
        print(f"   Age:  {person['age']}")

def print_entry_by_index(people_dict):
    index = get_number("the index of the entry you want to print")
    if 0 <= index < len(people_dict.keys()):
        for current_index, key in enumerate(people_dict):
            if current_index == index:
                entry = people_dict[key]
                print(f"ID: {key}")
                print(f"   Name: {entry['name']}")
                print(f"   Age: {entry['age']}")
            else:
                print("Error: index out of range.")


def exit_program():
    exit()

def main():
    people_dict = {}
    sum = 0
    avgList = [0,0]
    avgList[0] = 0
    avgList[1] = 0
    options = {
        "1": [save_entry,"Save a new entry_points."],
        "2": [search_by_id,"Search by ID."],
        "3": [print_avg_age,"Print ages average."],
        "4": [print_all_names,"Print all names."],
        "5": [print_all_ids, "Print all IDs."],
        "6": [print_all_entries,"Print all entries." ],
        "7": [print_entry_by_index, "Print entry by index."],
        "8": [exit_program,"Exit"]
        }
    while True:
        for menu_option in options:
            print(menu_option + ". " + options[menu_option][1])
        choice = input("Please enter your choice: ")
        match choice:
                    case "1":
                        save_entry(people_dict,avgList)
                    case "2":
                        search_by_id(people_dict)
                    case "3":
                        print_avg_age(avgList)
                    case "4":
                        print_all_names(people_dict)
                    case "5":
                        print_all_ids(people_dict)
                    case "6":
                        print_all_entries(people_dict)
                    case "7":
                        print_entry_by_index(people_dict)
                    case "8":
                        print("Exiting program.")
                        break
                    case _:
                        print("Invalid choice, Please enter a number from the menu..")
main()