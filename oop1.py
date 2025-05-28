class person:
    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def speak(self):
        print(self.name,"is speaking")
person1 = person("Mark",30,"teacher")
print(person1.name)
person1.speak()
print(person1.occupation)
print(person1.age)

person2 = person("Martha",40,"doctor")
print(person2.name)
person2.speak()
print(person2.occupation)
print(person2.age)


