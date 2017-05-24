def sum_row(n, column):
    objective = "O" + "_" + str(n) + str(column) + ": "
    for i in range(9):
        if i > 1:
            current = "+" + "A" + str(n) + "_" + str(column) + "_" + str(i)
            objective = objective + current
        else:
            current = "A" + str(n) + "_" + str(column) + "_" + str(i) + "+"
            objective = objective + current
    return objective 

def sum_column(n, row):
    objective = "O" + "_" + str(row) + str(n) + ": "
    for i in range(9):
        if i > 1:
            current = "+" + "A" + str(n) + "_" + str(i) + "_" + str(row)
            objective = objective + current
        else:
            current = "A" + str(n) + "_" + str(i) + "_" + str(row) + "+"
            objective = objective + current
    return objective 

    
def sum_matrixes(row, column):
    objective = "M" + "_" + str(row) + str(column) + ": "
    for i in range(9):
        if i > 1:
            current = "+" + "A" + str(i) + "_" + str(row) + "_" + str(column)
            objective = objective + current
        else:
            current = "A" + str(i) + "_" + str(row) + "_" + str(column) + "+"
            objective = objective + current
    return objective    


for l in range(9):
    for k in range(9):
        print (sum_matrixes(k, j))
        print(sum_column(l, k))
        print(sum_row(l, k))
