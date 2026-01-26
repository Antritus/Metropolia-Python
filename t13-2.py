class Racer:
    """Kilpailija: sisältää pisteet ja värin"""
    color = ""
    points = 0

    def __init__(self, color, points):
        self.color = color
        self.points = points

    def state(self):
        print("Olen", self.color, "ja minulla on", self.points, "pistettä!")

    def goal(self):
        self.points+=1

racer = Racer("sininen", 0)
racer.goal()
racer.state()