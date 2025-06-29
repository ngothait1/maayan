from Person import Person

class Student(Person):
    def __init__(self,ID,name,age,field_of_studies, year_of_study, average):
        super().__init__(ID,name,age)
        self.__field_of_studies = field_of_studies
        self.__year_of_study = year_of_study
        self.__average = average

    # --- Getters ---

    def getFieldOfStudies(self):
        return self.__field_of_studies

    def getYearOfStudy(self):
        return self.__year_of_study

    def getAverage(self):
        return self.__average

    # --- Setters ---

    def setFieldOfStudies(self, field_of_studies):
        self.__field_of_studies = field_of_studies

    def setYearOfStudy(self, year):
        if year >= 1:
            self.__year = year
        else:
            raise ValueError("at least 1 year")

    def setAverage(self, average):
        if 0 <= average <= 100:
            self.__average = average
        else:
            raise ValueError("avarage should be between 0-100")

    def to_dict(self):
        return {
            "type": "Student",
            "id": self.getID(),
            "name": self.getName(),
            "age": self.getAge(),
            "field_of_studies": self.getFieldOfStudies(),
            "year_of_study": self.getYearOfStudy(),
            "average": self.getAverage()
        }

    def print(self):
        super().print()
        print("The field of study is " + str(self.getFieldOfStudies()) + ", " + "The year of study " +str(self.getYearOfStudy()))

    def __str__(self):
        return f"{super().__str__()}\nField of study: {self.getFieldOfStudies()}, Year: {self.getYearOfStudy()}, Average: {self.getAverage()}"

