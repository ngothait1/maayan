
from Person import Person

class Employee(Person):
    def __init__(self,ID,name,age,field_of_work, salary):
        super().__init__(ID,name,age)
        self.__field_of_work = field_of_work
        self.__salary = salary

    # --- Getters ---
    def get_name(self):
        return self.__name

    def get_field_of_work(self):
        return self.__field_of_work

    def get_salary(self):
        return self.__salary

    # --- Setters ---
    def set_name(self, name):
        self.__name = name

    def set_field_of_work(self, field_of_work):
        self.__field_of_work = field_of_work

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            raise ValueError

    def to_dict(self):
        return {
            "type": "Employee",
            "id": self.getID(),
            "name": self.getName(),
            "age": self.getAge(),
            "field_of_work": self.get_field_of_work(),
            "salary": self.get_salary(),
            "field_of_studies": "",
            "year_of_study": "",
            "average": ""
        }

    def print(self):
        super().print()
        print(f"Field of work: {self.get_field_of_work()}, Salary: {self.get_salary()}")

    def __str__(self):
        return f"{super().__str__()}\nField of work: {self.get_field_of_work()}, Salary: {self.get_salary()}"
