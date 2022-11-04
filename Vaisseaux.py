from Armes import Weapon

class Vessel:
    def __init__(self,coordinates : tuple, max_hits : int, weapon : Weapon):
        self._coordinates = coordinates
        self._max_hits = max_hits
        self._weapon = Weapon

    def go_to(self,x:int,y:int,z:int):
        self._coordinates = [x,y,z]

    def get_coordinates(self,int,int,int):

    def fire_at(self,x:int,y:int,z:int):
        try:
            try:

            except
                print("OutOfRange")
                Weapon._ammunitions = Weapon._ammunitions - 1
        except self._max_hits ==0:
            print("DestroyedError")

class Cruiser(Vessel):
    def go_to(self,x:int,y:int,z:int):
        try:
            Vessel.get_coordinates(x,y,z)
        except z ==0:
            print("Déplacement impossible")

