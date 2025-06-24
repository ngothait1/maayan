class Person:
    def __init__(self,ID, name, age):
        self.__ID = ID
        self.__name = name
        self.__age = age

    def to_dict(self):
        return{
            "type": "Person",
            "id": self.getID(),
            "name": self.getName(),
            "age": self.getAge(),
            "field_of_work": "",
            "salary": "",
            "field_of_studies": "",
            "year_of_study": "",
            "average": ""
        }
    def getID(self):
        return self.__ID

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("Age must be non-negative")

    def print(self):
        print(f"The person {self.getName()} is {self.getAge()} years old")

    def __str__(self):
        return f"The person {self.getName()} is {self.getAge()} years old"



# if __name__ =="__main__":
#     test_name = "test_name"
#     test_age = 80
#     person = Person(test_name,test_age)
#     print(person.getAge())
#     if person.getAge() != test_age:
#         print("Error: Age should be " + str(test_age) + "but i got " + str(person.getAge()))
#     if person.getName() != test_name:
#         print("Error: Name should be " + test_name + "but i got " + person.getName())

