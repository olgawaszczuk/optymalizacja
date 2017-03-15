# Wypisuje funkcje celu
def getMaximize(n):
    maximize = "Maximize\nf : "
    for i in range(n):
        for j in range(n):
            current = "_" + str(i) + "_" + str(j)
            maximize = maximize + current + " + "
    return maximize[:-2] + "\n"


# Wypisuje zakresy wartosci zmiennych
def getBounds(n):
    bounds = "Bounds\n"
    for i in range(n):
        for j in range(n):
            current = "_" + str(i) + "_" + str(j)
            bounds = bounds + "0 <= " + current + " <= 1\n"
    return bounds + "\n"


# Wypisuje zmienne
def getGenerals(n):
    generals = "Generals\n"
    for i in range(n):
        for j in range(n):
            current = "_" + str(i) + "_" + str(j)
            generals = generals + current + "\n"
    return generals + "\n"


# Wypisuje ograniczenia funkcji
def getSubjectTo(n):
    subject_to = "Subject To\n"
    for i in range(n):
        subject_to = subject_to + column(i, n)
        subject_to = subject_to + row(i, n)

    for i in range(n - 1):
        subject_to = subject_to + diagonalDownLeft(i, n)
        subject_to = subject_to + diagonalDownRight(i, n)
        subject_to = subject_to + diagonalUpRight(i, n)
        subject_to = subject_to + diagonalUpLeft(i, n)
    return subject_to


# Wypisuje ograniczenia kolumn
def column(r, n):
    col_number = ""
    for i in range(n):
        col_number = col_number + "_" + str(r) + "_" + str(i) + " + "
    return col_number[:-2] + "<= 1\n"


# Wypisuje ograniczenia wierszy
def row(c, n):
    row_number = ""
    for i in range(n):
        row_number = row_number + "_" + str(i) + "_" + str(c) + " + "
    return row_number[:-2] + "<= 1\n"


# Wypisuje ograniczenia diagonali
def diagonalDownLeft(c, n):
    r = 0
    diagonal = ""
    for i in range(n - c):
        if r + i <= n - 1 and c - i >= 0:
            diagonal = diagonal + "_" + str(r + i) + "_" + str(c - i) + " + "
    return diagonal[:-2] + "<= 1\n"

def diagonalDownRight(c, n):
    r = 0
    diagonal = ""
    for i in range(n - c):
        if r + i <= n - 1 and c + i <= n - 1:
            diagonal = diagonal + "_" + str(r + i) + "_" + str(c + i) + " + "
    return diagonal[:-2] + "<= 1\n"

def diagonalUpLeft(c, n):
    r = n - 1
    diagonal = ""
    for i in range(n - c):
        if r - i >= 0 and c - i >= 0:
            diagonal = diagonal + "_" + str(r - i) + "_" + str(c - i) + " + "
    return diagonal[:-2] + "<= 1\n"

def diagonalUpRight(c, n):
    r = n - 1
    diagonal = ""
    for i in range(n - c):
        if r - i >= 0 and c + i <= n - 1:
            diagonal = diagonal + "_" + str(r - i) + "_" + str(c + i) + " + "
    return diagonal[:-2] + "<= 1\n"


# Wypisuje program liniowy
def getLinearProgram(n):
    if n < 1:
        return "Nieprawidlowe n. Podaj liczbe calkowita dodatnia >= 1"
    subjectTo = getSubjectTo(n)
    bounds = getBounds(n)
    generals = getGenerals(n)
    maximize = getMaximize(n)
    return maximize + subjectTo + bounds + generals


# Wpisz swoje n:
n = 5
print getLinearProgram(n)
