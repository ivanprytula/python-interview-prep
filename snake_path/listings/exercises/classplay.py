"""
Scipt for playing with classes - Object Oriented Programming
"""


class Aircraft:  # because planes and helicopters are awesome
    airspace = "troposphere"  # class variable shared in all instances

    def __init__(self, wingType, hours, vne, passengers):
        self.wingType = wingType
        self.hours = hours
        self.vne = vne  # Vne is the never exceed velocity - don't fly your plane faster than this!
        self.passengers = passengers

    def aircraftType(self):
        if self.wingType == "rotary":
            print("The aircraft is a helicopter")
        elif self.wingType == "fixed":
            print("The aircraft is an aeroplane")
        else:
            print("The aircraft type is unknown")

    def maintenance(self):
        strHours = str(self.hours)
        digits = len(strHours)
        tens = strHours[digits - 2 :]
        hrsRemain = 100 - int(tens)
        print("Hours until 100 hourly maintenance interval: ", hrsRemain)


# aeroplane Foxtrot X-ray Kilo
planeFXK = Aircraft("fixed", 2113, 180, 5)  # class instance = object
print("Airpsace: ", planeFXK.airspace)  # calling class variable
print("Wing: ", planeFXK.wingType)  # calling object attributes
print("Total Time in Service: ", planeFXK.hours)
print("Passengers: ", planeFXK.passengers)
planeFXK.aircraftType()  # calling object method
planeFXK.maintenance()

# helicopter Hotel Yankee Charlie:
heliHYC = Aircraft("rotary", 120, 130, 3)  # class instance = object
print("Airpspace: ", heliHYC.airspace)  # calling class variable
print("Wing: ", heliHYC.wingType)  # calling object attributes
print("Total Time In Service: ", heliHYC.hours)
print("Max passengers: ", heliHYC.passengers)
heliHYC.aircraftType()  # calling object method
heliHYC.maintenance()
