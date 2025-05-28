class Student:
    name = "Ann"
    gender = "Female"
    def study(self):
        print("Student is studying")
    def sleeping(self):
        print("Student is sleeping")
student1 = Student()  #creating an object
student1.study()
print(student1.name)
print(student1.gender)

student2 = Student()
student2.sleeping()
print(student2.name)
print(student2.gender)
