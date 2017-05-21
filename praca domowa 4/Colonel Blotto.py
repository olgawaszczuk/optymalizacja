#Założenia programu - Strategia wygrywająca: +1 punkt, remis: + 0,5 punkta, strategia przegrywająca: -1 punkt.
# Strategie gracza A: (2,2,2) z prawdopodobieństwem x1, (1,2,3) z prawdopodobieństwem x2, (1,1,4) z prawdopodobieństwem x3. Dla drugiego gracza analogiczne oznaczenia y1, y2, y3.

# Rozwiązanie w sage:
#Oryginalny problem:
print("Chcemy zmaksymalizować funkcję celu: y1(0.5x1 + 0.5x2 -x3) + y2(0.5x1 +0.5x2 + 0.5x3) + y3(x1 + 0.5x2 + 0.5x3)")

#Problem dualny:
matrixA = ([1, -0.5 , -0.5 , 1] , [1, -1, -0.5, -0.5], [1, -0.5, -0.5, -0.5], [0, 1, 1, 1], [0, 1, 1, 1])
vector_b = (0, 0, 0, 1, 1)
vector_c = (1, 0, 0, 0)

constraints = ["<=", "<=", "<=", "<=", ">="]
variables = ["", ">=", ">=", ">="]

P = InteractiveLPProblem(matrixA, vector_b, vector_c, ["z", "x1", "x2", "x3"], constraint_type = constraints, variable_type=variables)
show(P)

#Zamiana problemu do postaci normalnej
Pn = P.standard_form()
show(Pn)

show(Pn.run_simplex_method())



Poniżej rozwiązanie w solverze GLPK:
\* Problem: colonels *\

Maximize
obj: z

Subject To
c1: z - 0.5x1 - 0.5x2 + x3 <= 0
c2: z - 0.5x1 - 0.5x2 - 0.5x3 <= 0
c3: z - x1 - 0.5x2 + 0.5x3 <= 0
c4: x1 + x2 + x3 = 1

Bounds
0 <= x1 <= 1
0 <= x2 <= 1
0 <= x3 <= 1


Generals
x1
x2
x3


End
