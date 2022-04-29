class Orszag:



    def __init__(self, Város, Hely, ország):


        self.Város = str(Város)
        self.Hely = str(Hely)
        self.ország = str(ország)

    def rekordkép(self):
        txt = "\t" + self.Város+ " " + self.Hely +  " " + self.ország
        return txt
