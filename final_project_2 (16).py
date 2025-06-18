
import pandas as pd
from Person import Person
from Employee import Employee
from Student import Student
import json

def get_number(item_name):
    while True:
        user_input = input("Please enter " + item_name + ": ")
        if not user_input.isdigit():
            print("Error: " + item_name + " Must be a number, try again")
        else:
            return int(user_input)

def print_entry(person):
    print(person)
    # print(f"ID: {ID}")
    # print(f"   Name: {person['name']}")
    # print(f"   Age: {person['age']}")

def id_exist(people_dict, ID):
    return ID in people_dict

def save_entry(people_dict,people_list,avgList):
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
        while True:
            print("choose person type: ")
            print("1. Person")
            print("2. Employee")
            print("3. Student")
            choice = input("Please enter your choice, choice can be 1 | 2 | 3 ")
            match choice:
              case "1":
                 person = Person(ID, name, age)
                 break
              case "2":
                  field_of_work = input("Field of work: ")
                  salary = get_number("Salary")
                  person = Employee(ID, name, age, field_of_work,salary)
                  break
              case "3":
                  field_of_studies = input("What is your field of study? ")
                  year_of_study = get_number("Year of study")
                  average = float(input("what is your average study "))
                  person = Student(ID,name,age,field_of_studies,year_of_study,average)
                  break
              case _:
                 print("Please choose a valid option: 1, 2, or 3.")
        person = Person(ID, name, age)
        # person = {"name": name , "age": age}
        people_dict[ID] = person
        # people_list.append((ID,person))
        people_list.append(person)
        # print("type of people list: ",type(people_list))
        avgList[0] += age
        avgList[1] += 1
        print("ID ["+ str(ID) + "]Entry saved."   )
        break

def search_by_id(people_dict):
    ID = get_number("the ID you want to look for ")
    if int(ID) in people_dict:
        person = people_dict[ID]
        print_entry(person)
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
        person = people_dict[ID]
        print(f" {index}. {person.name}")

def print_all_ids(people_dict):
        for index, ID in enumerate(people_dict.keys()):
            print(f"{index}. {ID}")

def print_all_entries(people_dict):
    for index,(ID, person) in enumerate(people_dict.items()):
        print(f"{index}:")
        print_entry(person)

def print_entry_by_index(people_list):
    index = get_number("the index of the entry you want to print")
    if 0 <= index < len(people_list):
        person = people_list[index]
        print_entry(person)
    else:
        print("Error:index out of range.")
def read_column_names():
    with open("C:\\Users\\atiam\\PycharmProjects\\python project\\conf.json") as json_file:
        loaded = json.load(json_file)
        print(loaded)
        return loaded


def save_all_data(people_list):
     user_output_file_name=input("What is your output file name?")
     print("type of people_list:", type(people_list))
     print("people_list:", people_list)
     df = pd.DataFrame.from_records([p.to_dict() for p in people_list])

     column_map = read_column_names()
     df.rename(columns={
         'id': column_map.get('id','id'),
         'name': column_map.get('name','name'),
         'age': column_map.get('age','age')
     },inplace=True)


     df.to_csv(f"{user_output_file_name}.csv", index=False, mode='w')
     print(f"save print all data to {user_output_file_name}.csv")

def exit_program():
    exit()

def main():
    people_dict = {}
    people_list = []
    sum = 0
    avgList = [0,0]
    avgList[0] = 0
    avgList[1] = 0
    options = {
        "1": [save_entry,"Save a new entry."],
        "2": [search_by_id,"Search by ID."],
        "3": [print_avg_age,"Print ages average."],
        "4": [print_all_names,"Print all names."],
        "5": [print_all_ids, "Print all IDs."],
        "6": [print_all_entries,"Print all entries." ],
        "7": [print_entry_by_index, "Print entry by index."],
        "8": [save_all_data,"Save all data"],
        "9": [None,"Exit"]
        }
    while True:
        for menu_option in options:
            print(menu_option + ". " + options[menu_option][1])
        choice = input("Please enter your choice: ")
        match choice:
            case "1":
                save_entry(people_dict,people_list,avgList)
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
                print_entry_by_index(people_list)
            case "8":
                save_all_data(people_list)
            case "9":
                print("Exiting program.")
                exit()
            case _:
                print("Invalid choice, Please enter a number from the menu..")
main()