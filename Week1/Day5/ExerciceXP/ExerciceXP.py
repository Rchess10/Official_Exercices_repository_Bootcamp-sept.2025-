import math
from functools import total_ordering

@total_ordering
class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is None and diameter is None:
            raise ValueError("Either radius or diameter must be provided.")
        if radius is not None:
            self._radius = float(radius)
        else:
            self._radius = float(diameter) / 2.0

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = float(value)

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = float(value) / 2.0

    @property
    def area(self):
        return math.pi * (self._radius ** 2)

    def __str__(self):
        return f"Circle(radius={self._radius:.3f}, diameter={self.diameter:.3f})"

    def __repr__(self):
        return f"Circle(radius={self._radius!r})"

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(radius=self._radius + other._radius)

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return math.isclose(self._radius, other._radius, rel_tol=1e-9)

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius < other._radius


if __name__ == "__main__":
    # exemples d'utilisation (partie "main" — commentaires succincts pour expliquer)
    c1 = Circle(radius=2)          # cercle avec rayon 2
    c2 = Circle(diameter=6)        # cercle avec diamètre 6 -> rayon 3
    c3 = Circle(radius=2)          # même rayon que c1

    print(c1)                      # affiche les attributs du cercle
    print(f"area c2: {c2.area:.3f}")  # affiche l'aire

    # addition : crée un nouveau cercle dont le rayon est la somme des rayons
    c_sum = c1 + c2
    print("c1 + c2 ->", c_sum)

    # comparaisons
    print("c1 == c3 ?", c1 == c3)  # True
    print("c1 < c2 ?", c1 < c2)    # True

    # tri d'une liste de cercles
    circles = [c2, c_sum, c1, c3]
    circles.sort()
    # affiche la liste triée du plus petit au plus grand (par rayon)
    print("sorted radii:", [c.radius for c in circles])