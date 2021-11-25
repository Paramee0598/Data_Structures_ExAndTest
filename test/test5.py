class Rational:
    def __init__(self, n, d):
        self.n = n
        self.d = d
    def Rational():
        pass



print(" *** Rational Calculator ***")
print(" *        A = n1/d1        *")
print(" *        B = n2/d2        *")
print(" ***************************\n")

str_input = input("Enter n1 d1 n2 d2 : ")
n1, d1, n2, d2 = [int(e) for e in str_input.split()]
A = Rational(n1, d1)  # A = n1/d1
B = Rational(n2, d2)  # B = n2/d2
C = Rational()  # C = 1/1
print("A=", A, "B=", B)  # method __str__
print("A < B ==> ", A < B)  # method __lt__
print("A > B ==> ", A > B)  # method __gt__
print("A <= B ==> ", A <= B)  # method __ge__
print("A >= B ==> ", A >= B)  # method __ge__
print("A == B ==> ", A == B)  # method __eq__
print("A != B ==> ", A != B)  # method __ne__
print("A + B ==> ", A + B)  # method __add__
print("A - B ==> ", A - B)  # method __sub__
print("A * B ==> ", A * B)  # method __mul__
print("A / B ==> ", A / B)  # method __truediv__
print("A // B ==> ", A // B)  # method __floordiv__
print("A + C ==> ", A + C)