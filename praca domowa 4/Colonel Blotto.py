#Założenia programu - Strategia wygrywająca: +1 punkt, remis: + 0 punkta, strategia przegrywająca: -1 punkt.
# Strategie gracza A: xi - prawdopodobieństwa strategii.
# x1: (1,1,4), x2: (1,2,3), x3: (1,3,2), x4: (1,4,1), x5: (2,1,3), x6: (2,2,2), x7: (2, 3,1), x8: (3,1,2), x9: (3, 2,1), x10: (4, 1, 1)
#Dla drugiego gracza analogiczne oznaczenia y1, y2, y3, y4, y5, y6, y7, y8, y9, y10.

# Rozwiązanie w sage:
#Oryginalny problem:
print("Chcemy zmaksymalizować funkcję celu: y1(x6 + x7 + x9) + y2(x7 - x8 - x10) + y3(x4 - x9 - x10) + y4(x3 + x5 + x6 + x8) + y5(-x4 + x9) + y6(-x1 - x4 - x10) + y7(-x1 -x2 + x8) + y8(x2 - x4 + x7) + y9(-x1 + x3 - x5) + y10(x2 + x3 + x6)")

#Problem dualny:
matrixA = ([1,0,0,0,0,0,-1,-1,0,-1,0], [1,0,0,0,0,0,0,-1,1,0,1], [1,0,0,0,-1,0,0,0,0,1,1], [1,0,0,-1,0,-1,-1,0,-1,0,0],[1,0,0,0,1,0,0,0,0,-1,0],[1,1,0,0,1,0,0,0,0,0,1], [1,1,1,0,0,0,0,0,-1,0,0], [1,0,-1,0,1,0,0,-1,0,0,0], [1,1,0,-1,0,1,0,0,0,0,0], [1,0,-1,-1,0,0,-1,0,0,0,0], [0,1,1,1,1,1,1,1,1,1,1], [0,1,1,1,1,1,1,1,1,1,1])
vector_b = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1)
vector_c = (1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0)

constraints = ["<=", "<=", "<=", "<=","<=", "<=", "<=", "<=", "<=", "<=", "<=",">="]
variables = ["", ">=", ">=", ">=" , ">=" , ">=" , ">=" , ">=" , ">=", ">=", ">="]

P = InteractiveLPProblem(matrixA, vector_b, vector_c, ["z", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10"], constraint_type = constraints, variable_type=variables)
show(P)

#Zamiana problemu do postaci normalnej
Pn = P.standard_form()
show(Pn)

show(Pn.run_simplex_method())



