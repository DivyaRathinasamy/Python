
class Student:
    # Constructor
    def __init__(self,first_name,last_name,age,instructor,course):

    # Attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.instructor = instructor
        self.course = course

    # Method
    def print_info(self,message):
        print(message)
        print(f"Name: {self.first_name} {self.last_name}") 
        print(f"Age: {self.age}") 
        print(f"Instructor:{self.instructor}")
        print(f"Course:{self.course}")

class Course:
    def __init__(self,data):
        self.name = data["name"]
        self.instructors = data["instructors"]
        self.program = data["program"]

    #  Printing list of instructors
    def print_instructor_list(self):
        for instructor in self.instructors:
            print(instructor)
            # return self for chaining
            return self
        


    #  Updating particular instructor name
    def update_instructor(self,new_name,index):
        if index<len(self.instructors):
            self.instructors[index] = new_name
            return self

    def print_info(self):
        print(f"Program: {self.program}")
        print(f"Name:{self.name}")
        self.print_instructor_list()
        return self


python = {
    "name" : "Python/Flask",
    "instructors": ["Alfredo Salazar", "Spencer Rauch" ,"Tyler Tybault"],
    "program" : "Full Stack"

}

course_python = Course(python)
# Chaining
course_python.print_info().update_instructor("Ryan Mendaz" , 2).print_info()




# Creating an object  / Making an instance of the Student class
student_alex = Student("Alex","Martin","30","Lauren","Biology")
student_john = Student("John","Hilton","22","Aura","course_python")
# print(student_alex)


student_alex.print_info("Hey There")
student_john.print_info("I love you Daddy")

