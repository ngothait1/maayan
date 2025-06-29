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




