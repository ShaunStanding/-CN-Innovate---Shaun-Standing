# class Person():
#     def __init__(self, name):
#         self.name = name
class Person():
    def __init__(self, person_name, person_age, person_height):
        
        self.height = person_height
        self.age = person_age
        self.name = person_name
        self.hobbies = []

    def set_hair(self, person_hair):
        self.hair = person_hair
    
    def get_hair(self):
        print(self.hair)

    def set_hobby(self, hobby):
        self.hobbies.append(hobby)

    def get_hobby(self):
        print(f"{self.hobbies}")
        for hobby in self.hobbies:
            print(hobby)
        

# person_a = Person("shaun",20,"6ft")
# print(person_a.age)


# new_person = Person("Shaun")

# print(new_person)

