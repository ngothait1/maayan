from logging import exception
from math import trunc

import pandas as pd
from Person import Person
from Employee import Employee
from Student import Student
from enum import Enum

def get_number(item_name):
    while True:
        user_input = input("Please enter " + item_name + ": ")
        if not user_input.isdigit():
            print("Error: " + item_name + " Must be a number, try again")
        else:
            return int(user_input)

def get_name(item_name):
    while True:
        user_input = input(item_name)
        if not user_input.isalpha():
            print("Error: " + item_name + " must contain only letters ")
        else:
            return user_input

def get_valid_id(people_dict):
    while True:
        ID = get_number("ID")
        if ID in people_dict:
            print("This ID already exists. Entry not saved.")
        elif ID < 0:
            print("ID must be a positive number.")
        else:
            return ID
def get_valid_age():
    while True:
        age = get_number("Age")
        if 0 < age <= 120:
            return age
        else:
            print("Age must be between 1-120 and non-negative number.")

def choose_person_type(ID,name,age):
    while True:
        print("choose person type: ")
        print("1. Person")
        print("2. Employee")
        print("3. Student")
        choice = get_number("your choice, choice can be 1 | 2 | 3 ")
        match choice:
            case 1:
                return Person(ID, name, age)
            case 2:
                field_of_work = input("Field of work: ")
                salary = get_number("Salary")
                return Employee(ID, name, age, field_of_work, salary)
            case 3:
                field_of_studies = input("What is your field of study? ")
                year_of_study = get_number("Year of study")
                average = float(input("what is your average study "))
                return  Student(ID, name, age, field_of_studies, year_of_study, average)
            case _:
                print("Please choose a valid option: 1, 2, or 3.")

def save_entry(people_dict,people_list,avgList):
    ID = get_valid_id(people_dict)
    name = get_name("Please enter Name: ")
    age = get_valid_age()
    person = choose_person_type(ID, name, age)

    people_list.append(person)
    people_dict[ID] = person
    avgList[0] += age
    avgList[1] += 1
    print("ID ["+ str(ID) + "]Entry saved."   )

def search_by_id(people_dict):
    ID = get_number("the ID you want to look for ")
    if ID in people_dict:
        person = people_dict[ID]
        person.print(person)
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
        print(f" {index}. {person.getName()}")

def print_all_ids(people_dict):
        for index, ID in enumerate(people_dict.keys()):
            print(f"{index}. {ID}")

def print_all_entries(people_dict):
    for index,(ID, person) in enumerate(people_dict.items()):
        print(f"{index}: type = {type(person)}")
        person.print()

def print_entry_by_index(people_list):
    try:
        index = get_number("the index of the entry you want to print")
        if 0 <= index < len(people_list):
            person = people_list[index]
            person.print()
        else:
            print("Error:index out of range.")
    except Exception:
        print(f"Error printing entry")


def save_all_data(people_list):
    try:
         user_output_file_name=input("What is your output file name?")
         df = pd.DataFrame.from_records([p.to_dict() for p in people_list])
         df.to_csv(f"{user_output_file_name}.csv", index=False, mode='w')
         print(f"save print all data to {user_output_file_name}.csv")
    except Exception:
        print(f"Error saving data: ")

def exit_program():
    exit()

def main():
    try:
        people_dict = {}
        people_list = []
        sum = 0
        avgList = [0 , 0]
        avgList[0] = 0
        avgList[1] = 0

        class MenuOption(Enum):
            SAVE_ENTRY = "1"
            SEARCH_BY_ID = "2"
            PRINT_AVG_AGE = "3"
            PRINT_ALL_NAMES = "4"
            PRINT_ALL_IDS = "5"
            PRINT_ALL_ENTRIES = "6"
            PRINT_BY_INDEX = "7"
            SAVE_ALL_DATA = "8"
            EXIT = "9"
        while True:
            for option in MenuOption:
                 print(option.value + ". " + option.name.replace("_", " "))
            choice = input("Please enter your choice: ")
            match choice:
                case MenuOption.SAVE_ENTRY.value:
                    save_entry(people_dict,people_list,avgList)
                case MenuOption.SEARCH_BY_ID.value:
                    search_by_id(people_dict)
                case MenuOption.PRINT_AVG_AGE.value:
                    print_avg_age(avgList)
                case MenuOption.PRINT_ALL_NAMES.value:
                    print_all_names(people_dict)
                case MenuOption.PRINT_ALL_IDS.value:
                    print_all_ids(people_dict)
                case MenuOption.PRINT_ALL_ENTRIES.value:
                    print_all_entries(people_dict)
                case MenuOption.PRINT_BY_INDEX.value:
                    print_entry_by_index(people_list)
                case MenuOption.SAVE_ALL_DATA.value:
                    save_all_data(people_list)
                case MenuOption.EXIT.value:
                    print("Exiting program.")
                    exit()
                case _:
                    print("Invalid choice, Please enter a number from the menu..")
    except KeyboardInterrupt:
        print("Some error occurred ,Please rerun program")
main()