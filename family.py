class FamilyMember:
    def __init__(self, name, eye_colour, home_village):
        self.name = name
        self.eye_colour = eye_colour
        self.home_village = home_village

    def desc(self):
            return f"{self.name} has {self.eye_colour} eyes and {self.home_village} is their home village" 

member = FamilyMember("Alice", "blue", "Mukono")
print(member.desc())