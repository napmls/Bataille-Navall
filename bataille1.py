class Battlefield:
    def _init_(self):
        self.vessels = []

    def add_vessel(self,vessel):
        coor = vessel.get_coordinates()
        max_hits = vessel.max_hits
        for existing_vessel in self.vessels:
            if existing_vessel.get_coordinates() == coor:
                return False
            max_hits += existing_vessel.max_hits
        if max_hits > 22:
            return False
        self.vessels.append(vessel)

    def receive(self,x,y,z):
        coor = (x,y,z)
        for existing_vessel in self.vessels:
            if existing_vessel.get_coordinates() == coor:
                return True
        return False