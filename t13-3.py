class Racer:
    """Kilpailija: sisältää pisteet ja värin"""
    color = ""
    points = 0

    def __init__(self):
        self.color = input("Anna minulle väri:")

    def state(self):
        print("Olen", self.color, "ja minulla on", self.points, "pistettä!")

    def goal(self):
        self.points+=1

racer1 = Racer()
racer2 = Racer()
racer1.state()
racer2.state()
print(Racer.__doc__)