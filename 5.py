a = {12,2,0,3,8}
b = {15,10,12,3,6}
# Difference: only elements in b that are not in a
difference = b.difference(a)
# Symmetric difference: elements in either set but not both
symmetric_difference = b.symmetric_difference(a)

print(f"The difference is {difference} and The symmetric difference is {symmetric_difference}")
