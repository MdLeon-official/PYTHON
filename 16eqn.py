
#d+a+2ab/d(4c+10)

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

lhs = d+a+(2*a*b)
rhs = d*(4*c + 10)

print(f"d+a+2ab/d(4c+10) = {lhs/rhs:.3f}")
