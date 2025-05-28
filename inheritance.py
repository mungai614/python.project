#super/parent/base class
class Animal:
    def speak(self):
        print('Animal is speaking')
#child class/sub class/derived class
class Dog(Animal):
    def bark(self):
        print('Dog is barking')
class cat(Dog):
    def meow(self):
        print('Cat is meowing')

a = Animal()
a.speak()
d = Dog()
d.speak()
d.bark()
c = cat()
c.meow()

