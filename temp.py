class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    # used to find length
    def __len__(self):
        return len(self.name)
    
    # used for return value when obj is created
    def __repr__(self):
        print('repr is called')
        return str({
            "name":self.name,
            "age":self.age
        })
    
    # used for print(), takes priority over repr when both are defined
    def __str__(self):
        return "Object created successfully"


s1 = Student('Kartikey',24)
s2 = Student('Kartikey',24)

print(s1) # __repr__ is used if __str__ is not defined
print(s1)  # __str__ is used when both __str__ and __repr__ are defined

print(len(s1))
