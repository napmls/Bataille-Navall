
class Weapon:
    def __init__(self,ammunitions: int, range: int):
        self._ammunitions = ammunitions
        self._range = range

class Missile_anti_surface(Weapon):
    def fire_at(x:int,y:int,z:int):
        try:
            try:
                print(f"feu sur le point {x},{y},{z}")
                Weapon._ammunitions = Weapon._ammunitions - 1
            except Weapon._ammunitions == 0 :
                print("NoAmmunationError")
        except z != 0:
            print("OutOFRangeError")
            Weapon._ammunitions = Weapon._ammunitions - 1

class Missile_anti_air(Weapon):
    def fire_at(x:int,y:int,z:int):
        try:
            try:
                print(f"feu sur le point {x},{y},{z}")
                Weapon._ammunitions = Weapon._ammunitions - 1
            except Weapon._ammunitions == 0 :
                print("NoAmmunationError")
        except z <=0 :
            print("OutOFRangeError")
            Weapon._ammunitions = Weapon._ammunitions - 1

class Torpille(Weapon):
    def fire_at(x:int,y:int,z:int):
        try:
            try:
                print(f"feu sur le point {x},{y},{z}")
                Weapon._ammunitions = Weapon._ammunitions - 1
            except Weapon._ammunitions == 0 :
                print("NoAmmunationError")
        except z >0 :
            print("OutOFRangeError")
            Weapon._ammunitions = Weapon._ammunitions - 1