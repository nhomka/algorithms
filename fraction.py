from fraction_helpers import gcd
class Fraction:

    def __init__(self, top, bottom):
        top, bottom = self.validate(top, bottom)

        t = gcd(top, bottom)
        self.num = top//t
        self.den = bottom//t

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self})"

    def __add__(self, f2):
        f1 = self
        f2 = Fraction((f1.num*f2.den) + (f2.num*f1.den), (f1.den*f2.den))

        # Since we reduce fractions upon initialization, we no longer need to do so
        #t = gcd(f2.num, f2.den)
        #f2.num, f2.den = f2.num//t, f2.den//t

        return f2

    def __radd__(self, f2):
        return self + f2

    def __iadd__(self, f2):
        self = self + f2
        return self

    def __sub__(self, f2):
        f1 = self
        res = Fraction((f1.num*f2.den) - (f2.num*f1.den), (f1.den*f2.den))
        t = gcd(res.num, res.den)
        res.num, res.den = res.num//t, res.den//t
        return res

    def __mul__(self, f2):
        f1 = self
        res = Fraction(f1.num*f2.num, f1.den*f2.den)
        t = gcd(res.num, res.den)
        res.num, res.den = res.num//t, res.den//t
        return res

    def __truediv__(self, f2):
        f1 = self
        f3 = Fraction(f2.den, f2.num)
        return f1*f3

    def __lt__(self, f2):
        return self.num/self.den < f2.num/f2.den

    def __le__(self, f2):
        return self.num/self.den <= f2.num/f2.den

    def __gt__(self, f2):
        return self.num/self.den > f2.num/f2.den

    def __ge__(self, f2):
        return self.num/self.den >= f2.num/f2.den
    
    def __eq__(self, f2):
        return (self.num * f2.den) == (self.den * f2.num)
    
    def __ne__(self, f2):
        return (self.num * f2.den) != (self.den * f2.num)

    def validate(self, a ,b):
        try:
            _ = a + 1, b + 1
        except:
            print("Improper input type")

        if int(a) != a or int(b) != b:
            raise RuntimeError("Both inputs must be integers")

        a = -a if b < 0 else a
        b = abs(b)
        return (a, b)

        


f1 = Fraction(1, 8)
f2 = Fraction(1, 2)
f3 = f2/f1
print(f3, f1 < f2, f1 > f2, f3 < f1, f3 > f2)
f4 = Fraction(-1, 1)
f5 = Fraction(2, -4)
f6 = Fraction(-1, -4)
print(f4, f5, f6)
f4 += f5
print(f4, repr(f4))