class Common_Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def check(self):
        if self.numerator <= self.denominator:
            print("Дріб є правильним")
        else:
            False

fraction = Common_Fraction(3, 5)
print(fraction.check())