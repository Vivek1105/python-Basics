class Students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Students("sunny",16,"8th")
student2 = Students("vishal",17,"7th")
# print(hasattr(student2,"grade"))     # "hasattr" use to chek the attribuets are present or not
# print(hasattr(student2,"sem"))
# setattr(student2,"sem","9th")        # "setattr" use to set the attribuets
# print(hasattr(student2,"sem"))
#
# print(getattr(student1,"age"))      # "getattr" use to chekmthe exact attribuets
print(student2.age)

delattr(student1,"name")
print(hasattr(student1,"name"))     # "delattr" use to delete an attibuets