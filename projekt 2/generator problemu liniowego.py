#Poniżej wprowadzamy dane do problemu.
dane= \
"""\
16 19 1 1
18 13 0 0
17 16 0 1
17 6 1 0
11 10 1 1
2 3 1 0
12 11 0 2
17 11 0 1
4 18 0 0
8 10 0 5
17 10 0 9
11 10 6 1
17 17 0 1
0 2 0 1
7 15 1 0
11 6 0 1
19 9 0 2
11 10 4 0
10 16 0 1
17 13 1 0\
    """
n = 20
matrix = []
i = 0
j = 0

# Zapisujemy dane do postaci tabeli:
for line in dane.split("\n"):
    current = []
    for element in line.strip("\r").split(" "):
        try:
            current.append(int(element))
        except ValueError:
            pass
    matrix.append(current)

# Funkcja licząca ilu podwładnych (łącznie z sobą) ma dany pracownik (boss_i) w wybranej (tree):
def count(tree, boss_i, matrix):
    number = 1
    for node_i in range(len(matrix)):
        if node_i == boss_i:
            continue
        if matrix[node_i][tree] == boss_i:
            number += count(tree, node_i, matrix)
    return number

# Funkcja wypisująca podwładnych, których pracownik ma w ramach wybranej organizacji:
def get_employees_under_boss(boss_id, tree, matrix):
    employees_index_list = []
    for node in matrix:
        if node[tree] == boss_id:
            if not matrix.index(node) == boss_id:
                employees_index_list.append(matrix.index(node))
    return list(set(employees_index_list))

# Funkcja zwracająca słownik opisujący strukturę wybranej organizacji, tzn taki, w którym do każdego pracownika przypisane zostają: 
#"Self" - jego własny indeks, "Count" - liczba jego podwładnych,
#"ToFire" - maksymalna liczba jego podwładnych (łącznie z nim), która może zostać zwolniona, "Tree" - organizację dla której opisywana jest hierarchia,
#"Boss" - indeks szefa tego pracownika, "Employees" - listę podwładnych tego pracownika (bez niego):
def get_employees_lists(tree, matrix):
    employees_list = []
    for node_i in range(len(matrix)):
        number_of_employees = {"Self": node_i,
                              "Count": count(tree, node_i, matrix),
                               "ToFire": count(tree, node_i, matrix) - matrix[node_i][tree + 2],
                               "Tree": tree,
                               "Boss": matrix[node_i][tree],
                               "Employees": get_employees_under_boss(node_i, tree, matrix)}
        employees_list.append(number_of_employees)
    return employees_list

# Funkcja zwracająca tekst będący funkcją celu programu liniowego:
def getSelfObjectiveFunction(employee_list):
  string = ""
  for boss in employee_list:
        boss_index = employee_list.index(boss)
        string += "eb_" + str(boss_index) + "e_" + str(boss_index) + " + "
  return string[:-2]

# Funkcja zwracająca tekst będący ograniczeniami typu a (dopkładny opis ograniczeń i zmiennych zawarty jest w raporcie) programu liniowego:
def getCapacityConstraint(employee_list):
    string = ""
    for boss in employee_list:
        boss_index = employee_list.index(boss)
        string += "eb_" + str(boss_index) + "e_" + str(boss_index) + " + "
        for employee in boss["Employees"]:
            string += "eb_" + str(boss_index) + "e_" + str(employee) + "_" + str(employee_list[boss_index]["Tree"]) + " + "
        string = string[:-2] + "<= " + str(employee_list[boss_index]["ToFire"]) + "\n"
    return string

# Funkcja zwracająca tekst będący ograniczeniami typu b programu liniowego:
def getConservationConstraint(employee_list):
    string = ""
    for boss in employee_list:
        boss_index = employee_list.index(boss)
        string += "eb_" + str(boss_index) + "e_" + str(boss_index) + " + "
        for employee in boss["Employees"]:
            string += "eb_" + str(boss_index) + "e_" + str(employee)  + "_" + str(employee_list[boss_index]["Tree"]) + " + "
        if(boss_index == employee_list[boss_index]["Boss"]):
            string = string[:-2] + " <= " + str(employee_list[boss_index]["ToFire"]) + "\n"
        else:
            string = string[:-2] + "- eb_" + str(employee_list[boss_index]["Boss"]) + "e_" + str(boss_index) + "_" +  str(employee_list[boss_index]["Tree"]) +  " = 0\n"

    return string

# Funkcja zwracająca tekst będący ograniczeniami dla zmiennych pierwszego typu programu liniowego:
def getSelfBounds(employee_list):
  string = ""
  for boss in employee_list:
    boss_index = employee_list.index(boss)
    string += "0 <= " +  "eb_" + str(boss_index) + "e_" + str(boss_index) + " <= 1 \n"
  return string
 
# Funkcja zwracająca tekst będący ograniczeniami dla zmiennych drugiego typu (krawędzi) programu liniowego:
def getBounds(employee_list):
    string = ""
    for boss in employee_list:
        boss_index = employee_list.index(boss)
        for employee in boss["Employees"]:
           toFire = employee_list[employee]["ToFire"]
           string += "0 <= eb_" + str(boss_index) + "e_" + str(employee) + "_" + str(employee_list[boss_index]["Tree"]) + " <= " + str(toFire) + "\n"
    return string

# Funkcja wypisująca zmienne pierwszego typu:
def getSelfGenerals(employee_list):
  string = ""
  for boss in employee_list:
      boss_index = employee_list.index(boss)
      string += "eb_" + str(boss_index) + "e_" + str(boss_index) + "\n" 
  return string

# Funkcja wypisująca zmienne drugiego typu:
def getGenerals(employee_list):
    string = ""
    for boss in employee_list:
        boss_index = employee_list.index(boss)
        for employee in boss["Employees"]:
            string += "eb_" + str(boss_index) + "e_" + str(employee) + "_" + str(employee_list[boss_index]["Tree"]) + "\n"
    return string


# Przypisanie drzew do odpowiedniej struktury organizacji:
tree0 = get_employees_lists(0, matrix)
tree1 = get_employees_lists(1, matrix)

# Wypisywanie problemu liniowego:
print "\nMaximize"
print getSelfObjectiveFunction(tree0)
print "\nSubject To"
print getCapacityConstraint(tree0)
print getCapacityConstraint(tree1)
print getConservationConstraint(tree0)
print getConservationConstraint(tree1)
print "\nBounds"
print getSelfBounds(tree0)
print getBounds(tree0)
print getBounds(tree1)
print "\nGenerals"
print getSelfGenerals(tree0)
print getGenerals(tree0)
print getGenerals(tree1)
print "\nEnd"

#Uwaga techniczna : program pisany jest pod kompilator języka Python, nie pod Sage.
