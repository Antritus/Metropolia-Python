class Racer:
    color = ""
    points = 0

    def __init__(self, color, points):
        self.color = color
        self.points = points


racer = Racer("sininen", 10)
print("Kilpailijalla", racer.color, "on", racer.points, "pistettä!")