import math


class Ulamek:
    __slots__ = ('licznik', 'mianownik')

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


Lista_Ulamkow = []
n = 3000000
for i in range (n):
    A = Ulamek(i, i + 1)
    Lista_Ulamkow.append(A)

for i in range (n - 1):
    Lista_Ulamkow[i].add(Lista_Ulamkow[i + 1])

#print(Lista_Ulamkow)