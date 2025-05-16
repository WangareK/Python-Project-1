class Students:
    #Class attributes
    school="GOMYCODE"
    def __init__(self,age, course, name, gender):
        self.age=age
        self.course= course
        self.name=name
        self.gender=gender
    def get_age(self):
        return self.age
    def get_course(self):
        return self.course
    def get_name(self):
        return self.name
    def get_gender(self):
        return self.gender
    def set_name(self,n):
        self.name=n
    def set_age(self,a):
        self.age=a+2
    def set_course(self,c):
        self.course=c
    def set_gender(self,g):
        self.gender=g
# Student1=Students(21,"Data Science","Kyalo","Male")
# student_name=Student1.get_name()
# print(student_name)
name=input("Enter your full name")
age=int(input("Please enter your age"))
course=input("Please enter your course name")
gender=input("Please enter your gender")
Student1=Students(age,course,name, gender)
print("The student's name is:",Student1.name)
print("The student's age is:",Student1.get_age())
print("The student's course is:",Student1.course)
print("The student is:",Student1.gender)

class Pupil(Students):
    def __init__(self,name,grade,position):
        super().__init__(age,course,name, gender)
        self.grade=grade
        self.position=position



