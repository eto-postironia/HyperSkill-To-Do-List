class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        if self.a * self.a + self.b * self.b == self.c * self.c:
            self.area = self.a * self.b / 2.0
            print(self.area)
        else:
            print("Not right")


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

right_triangle = RightTriangle(input_c, input_a, input_b)
