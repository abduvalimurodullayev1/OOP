class Ronaldo:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def speak(self):
        return f"Hello, I'm {self.first_name} {self.last_name}"

# Derived classes


class Jr(Ronaldo):
    def __init__(self, first_name):

        super().__init__(first_name, "Ronaldo Jr.", 0)

    def speak(self):
        return f"Hello, I'm {self.first_name} {self.last_name}, Jr."


class JR2(Ronaldo):
    def __init__(self, first_name):

        super().__init__(first_name, "Ronaldo Jr. 2", 0)

    def speak(self):
        return f"Hello, I'm {self.first_name} {self.last_name} Jr. 2"


rf = Jr("Junior")
rg = JR2("Junior2")


print(rf.first_name)
print(rf.speak())

print(rg.first_name)
print(rg.speak())
