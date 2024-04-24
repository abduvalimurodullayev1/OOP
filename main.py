# class Student:
#     def __init__(self, age, name, surname, id, girlfriend, friend):
#         self.age = age
#         self.name = name
#         self.surname = surname
#         self.id = id
#         self.girlfriend = girlfriend
#         self.friend = friend
#
#     def student_information(self):
#         """Show information about the student."""
#         print(f"Age:{self.age}")
#         print(f"Name:{self.name}")
#         print(f"Surname:{self.surname}")
#         print(f"Id:{self.id}")
#         print(f"GirlFriend:{self.girlfriend}")
#         print(f"Friend:{self.friend}")
#
#
# oybek = Student("Oybek", 17, "Yuldoshev", 1, "if i say he cry", "I don't know" )
# baxtiyor = Student("Baxtiyor", 17, "Gopporov", 2, "I don't know", "I don't know" )
# Muzaffar = Student("Muzaffar", 17, "Ergashev", 3, "secret", "I don't know" )
# Aburayhon = Student("Aburayhon", 17, "Eshqulov", 4, "Somebody", "I don't know" )
#
# oybek.student_information()
# baxtiyor.student_information()
# Muzaffar.student_information()
# Aburayhon.student_information()
#


class Footballer:
    def __init__(self, name, shoot, foot, heading, ball_control, strength, speed, passing, iq, defending):
        self.name = name
        self.shoot = shoot
        self.foot = foot
        self.heading = heading
        self.ball_control = ball_control
        self.strength = strength
        self.speed = speed
        self.passing = passing
        self.iq = iq
        self.defending = defending

    def footballer_ability_information(self):
        """Footballer show the information"""
        print(f"Name:{self.name}")
        print(f"shoot:{self.shoot}")
        print(f"foot:{self.foot}")
        print(f"heading:{self.heading}")
        print(f"ball_control:{self.ball_control}")
        print(f"strength:{self.strength}")
        print(f"passing:{self.passing}")
        print(f"iq:{self.iq}")
        print(f"Defending:{self.defending}")


ronaldo = Footballer("Cristiano Ronaldo", 104, "both_foot", 102, 95, 87, 90, 89, 90, 20)
ramos = Footballer("Sergio Ramos", 76, "right_foot", 98, 77, 100, 80, 70, 76, 105)
messi = Footballer("Leonel Messi", 99, "left_foot", 77, 100, 72, 93, 93, 92, 10)
carles = Footballer("Carles Puyol", 65, "right_foot", 97, 85, 99, 80, 75, 80, 104)
erling = Footballer("Erling Haaland", 102, "left_foot", 100, 85, 103, 76, 70, 70, 56)
ruben = Footballer("Ruben Dias ", 56, "right_foot", 96, 75, 102, 86, 76, 70, 103)

ronaldo.footballer_ability_information()
ramos.footballer_ability_information()
messi.footballer_ability_information()
carles.footballer_ability_information()
erling.footballer_ability_information()
ruben.footballer_ability_information()








