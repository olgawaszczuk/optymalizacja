#Problem dualny
matrixA = ([1, 0 , -1 , 1] , [1, 1, 0, -1], [1, -1, 1, 0], [0, 1, 1, 1] ,[0, 1, 1, 1])
vector_b = (0, 0, 0,1, 1)
vector_c = (1, 0, 0, 0)

constraints = ["<=", "<=", "<=", "<=", ">="]
variables = ["", ">=", ">=", ">="]

P = InteractiveLPProblem(matrixA, vector_b, vector_c, ["z", "x1", "x2", "x3"], constraint_type = constraints, variable_type=variables)
show(P)

#Zamiana problemu do postaci normalnej
Pn = P.standard_form()
show(Pn)

show(Pn.run_simplex_method())
