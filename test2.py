class User:
    def __init__(self):
        self.currentUser = None
    def initialise_male(self, name, weight, height, age):
        print(age)
        user = Male(name,weight,height,age)
        self.currentUser= user 
        
    # def initialise_female(self, name, weight, height, age):
    #     user = Female(name,weight,height,age)
    #     self.currentUser= user 
    def get_age(self):
        return self.currentUser.age

class Male:
    def __init__(self,name,weight,height,age):
        self.height = height
        self.name = name
        self.weight = weight
        self.age = age
        self.calories = 2000 
def Main():
    User.(  )
