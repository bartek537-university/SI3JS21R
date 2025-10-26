import math


class Kolo:
    def __init__(self, radius: float):
        self.radius = radius

    def oblicz_pole(self) -> float:
        return math.pi * self.radius ** 2

    def oblicz_obwod(self) -> float:
        return 2 * math.pi * self.radius


kolo = Kolo(3)
print(kolo.oblicz_pole())
print(kolo.oblicz_obwod())
