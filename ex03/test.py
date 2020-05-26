from matrix import Matrix

print("1st initialization")
m1 = Matrix([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0],
            [6.0, 7.0, 8.0], [9.0, 10.0, 11.0]])
print(m1)
print("------------------------------------------------------------")
print("2nd initialization")
m2 = Matrix((2, 4))
print(m2)
print("-----------------------------------------------------------")
print("3d initialization")
m3 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]], (3, 2))
print(m3)

print("-----------------------------------------------------------")
print(" Bad initialization")
m4 = Matrix((1, 3), (2, 5))
print("-----------------------------------------------------------")
print("Additions")
m4 = m3 + m3
print(m4)
print(m3 + m4)
print(m4 + m3)
print("-----------------------------------------------------------")
