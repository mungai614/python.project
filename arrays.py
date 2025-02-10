# courss
courses = ["MIT","Cybersecurity","Datascience"]
print(courses)

#ACCESSING AN ELEMENT
print(courses[2])

#looping through an array
for a in courses:
    print("Course is",a)

#adding a new element into an array
courses.append("Laravel")
print(courses)

#deleting an element from an array
courses.remove("Cybersecurity")
print(courses)