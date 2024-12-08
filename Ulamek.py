import math


class Ulamek:
    licznik = 0
    mianownik = 1

    def __init__(self, licznik, mianownik):
        assert (mianownik != 0)
        self.licznik = licznik
        self.mianownik = mianownik

    def __str__(self):
        return f'{int(self.licznik)}/{int(self.mianownik)}'

    def __repr__(self):
        return f'{int(self.licznik)}/{int(self.mianownik)}'

    def simplify(self):
        assert (self.mianownik != 0)
        gcd = int(math.gcd(int(self.licznik), int(self.mianownik)))
        self.licznik /= gcd
        self.mianownik /= gcd
        if self.licznik < 0 and self.mianownik < 0:
            self.licznik *= -1
            self.mianownik *= -1

    def __eq__(self, other):
        self.simplify()
        other.simplify()
        return self.mianownik == other.mianownik and self.licznik == other.licznik

    def __lt__(self, other):
        return self.licznik / self.mianownik < other.licznik / other.mianownik

    def __gt__(self, other):
        return self.licznik / self.mianownik > other.licznik

    def __le__(self, other):
        return self.licznik / self.mianownik <= other.licznik

    def __ge__(self, other):
        return self.licznik / self.mianownik >= other.licznik

    def __ne__(self, other):
        self.simplify()
        other.simplify()
        return self.mianownik != other.mianownik or self.licznik != other.licznik

    def add(self, A):
        assert (A.mianownik != 0)
        self.licznik *= A.mianownik
        self.licznik += A.licznik * self.mianownik
        self.mianownik *= A.mianownik
        self.simplify()

    def subtract(self, A):
        assert (A.mianownik != 0)
        self.licznik *= A.mianownik
        self.licznik -= A.licznik * self.mianownik
        self.mianownik *= A.mianownik
        self.simplify()

    def multiply(self, A):
        assert (A.mianownik != 0)
        self.licznik *= A.licznik
        self.mianownik *= A.mianownik
        self.simplify()

    def divide(self, A):
        assert (A.mianownik != 0)
        self.licznik *= A.mianownik
        self.mianownik *= A.licznik
        self.simplify()


A = Ulamek(6, 10)
A.simplify()
print(A)
B = Ulamek(2, 7)
A.add(B)
assert A.licznik == 31 and A.mianownik == 35
A.multiply(B)
A.multiply(B)
print(A)
assert A.licznik == 124 and A.mianownik == 1715
assert A > B



