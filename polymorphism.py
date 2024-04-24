class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def move(self):
        print("Swim")


class Plane:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def move(self):
        print("Fly")


car1 = Car("Matiz", "Chevrolet")
boat1 = Boat("Titanic", "nimadir")
plane1 = Plane("Boing747", "Boeng")
for x in (car1, boat1, plane1):
    x.move()