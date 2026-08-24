class Triangle:

    def __init__(self, base, height):
        self._base = base
        self._height = height

    @property
    def base(self):
        return f"{self._base:.2f}"

    @property
    def height(self):
        return f"{self._height:.2f}"

    @base.setter
    def base(self, new_base):
        if new_base > 0:
            self._base = new_base

    @base.deleter
    def base(self):
        del self._base

    @height.deleter
    def height(self):
        del self._height

    def area(self):
        return 1/2 * (self._base * self._height)

triangle = Triangle(2.5, 4.5)

print(triangle.base)
print(triangle.height)
print(triangle.area())

triangle.base = 12
print(triangle.base)

del triangle.base
del triangle.height

