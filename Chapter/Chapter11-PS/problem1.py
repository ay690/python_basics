class Twovector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class ThreeVector(Twovector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k


    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")



a = Twovector(7, 2)
a.show()
b = ThreeVector(6, 7, 4)
b.show()