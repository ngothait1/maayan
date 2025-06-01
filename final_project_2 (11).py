
my_dict = {}
def save_entry():
    ID =  input("ID: ")
    name = input("Name: ")
    age = input("Age: ")
    my_dict[ID] = {
        "name": name,
        "age": int(age)
    }


# def save_entries():
#     save_entry_auto('1', 'name 1', '12')
#     save_entry_auto('2', 'name 2', '13')
#     save_entry_auto('3', 'name 3', '14')


def save_entry_auto(id, name, age):
    my_dict[id] = {
        "name": name,
        "age": int(age)
    }


def search_by_id():

    ID_input = input("Please enter the ID you want to look for: ")
    try:
        ID = str(int(ID_input))
    except ValueError:
        print(f"Error: ID must be a number. {ID_input} is not a number.")
        return

    if ID in my_dict:
        print(f"ID: {ID}")
        print(f"Name: {my_dict[ID]['name']}")
        print(f"Age: {my_dict[ID]['age']}")
    else:
        print("not exist")

def print_avg_age():
    sum = 0
    for item in my_dict.values():
        sum += item.get("age")
    avg = int(sum/len(my_dict))
    print(avg)


def print_all_names():
    new_names = [item["name"] for item in my_dict.values()]
    for index, ID in enumerate(new_names):
        print(f" {index}. {ID}")

def print_all_ids():
    ids = list(my_dict.keys())
    for index, ID in enumerate(ids):
        print(f"{index}. {ID}")

def print_all_entries():
    entries = list(my_dict.items())
    for index,(ID, person) in enumerate(entries):
        print(f"{index}, {ID}")
        print(f"   Name: {person['name']}")
        print(f"   Age:  {person['age']}")

def print_entry_by_index():
    ids = list(my_dict.keys())
    user_input = input("Please enter the index of the entry you want to print: ")

    try:
        index = int(user_input)
    except ValueError:
        print(f"Error: index must be a number. {user_input} is not a number.")
        return

    if 0 <= index < len(ids):
        ID = ids[index]
        entry = my_dict[ID]
        print(f"ID: {ID}")
        print(f"   Name: {entry['name']}")
        print(f"   Age: {entry['age']}")
    else:
        print("Error: index out of range.")


def exit_program():
    exit()

options = {
    "1": save_entry,
    "2": search_by_id,
    "3": print_avg_age,
    "4": print_all_names,
    "5": print_all_ids,
    "6": print_all_entries,
    "7": print_entry_by_index,
    "8": exit_program
}
while True:
    choices = [ "1. Save a new entry_points.",
     "2. Search by ID.",
     "3. Print ages average.",
     "4. Print all names.",
     "5. Print all IDs.",
     "6. Print all entries.",
     "7. Print entry by index.",
     "8. Exit."]
    print("\n".join(choices))
    choice = input("Please enter your choice: ")
    options[choice]()
    input("Press Enter to continue ")
    print(my_dict)