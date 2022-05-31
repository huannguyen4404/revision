class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def __str__(self):
        return "This is a human of name " + self.name + " and age " + str(self.age)


me = Human("Angel", 99)
name = me.getname()
age = me.getage()
# print(f"{name}: {age} years old")
print(me)
