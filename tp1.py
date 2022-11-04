class OutOfRangeError(Exception):
    pass

class NoAmmunitionError(Exception):
    pass

class Weapon:
    def __init__(self, ammunition: int, range: int):
        self._ammunition=ammunition
        self._range=range
    def fire_at(self, x: int, y: int, z: int):
        if self._ammunition != 0 :
            self._ammunition = self._ammunition-1
        else :
            raise NoAmmunitionError

class Lance_missiles_antisurface(Weapon):
    def __init__(self):
        self._ammunition= 3
        self._range= 30


    def fire_at(self, x: int, y: int,z : int):
        if z == 0:
            if self._ammunition != 0 :
                self._ammunition = self._ammunition-1
            else :
                raise NoAmmunitionError
        else : 
            raise OutOfRangeError


class Lance_missiles_antiair(Weapon):
    def __init__(self):
        self._ammunition= 50
        self._range= 40


    def fire_at(self, x: int, y: int, z: int): 
        if z>0:
            if self._ammunition != 0 :
                self._ammunition = self._ammunition-1
            else :
                raise NoAmmunitionError
        else:
            raise OutOfRangeError


class Lance_Torpilles(Weapon):
    def __init__(self):
        self._ammunition= 15
        self._range= 20


    def fire_at(self, x: int, y: int, z: int):
        if z<0:
            if self._ammunition != 0 :
                self._ammunition = self._ammunition-1
            else :
                raise NoAmmunitionError