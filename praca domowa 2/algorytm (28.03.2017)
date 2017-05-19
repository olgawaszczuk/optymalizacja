import itertools
import numpy

# Funkcja tworząca macierz kwadratową z kolumn indeksowanych w zbiorze możliwych kombinacji
def getMatrix(matrixA, cols):
    matrix = []

    for row in range(len(matrixA)):
        matrix.append([])

    for i in range(len(matrix)):
        for j in range(len(cols)):
            matrix[i].append(matrixA[i][cols[j]])

    return matrix

#Funkcja sprawdzająca czy macierz jest osobliwa
def isZero(matrix):
    npmatrix = numpy.array(matrix)
    return numpy.linalg.det(npmatrix) == 0

#Funkcja generująca rozwiązanie układu równań
def getResult(vector, matrix):
    npmatrix = numpy.array(matrix)
    npvector = numpy.array(vector)
    result = numpy.linalg.solve(npmatrix, npvector).tolist()
    return result

#Funkcja przedłużająca rozwiązanie układu równań do wektora o wymiarze liczby wejściowych zmiennych
def getFinalVector(vector, collumnNumbers, length):
    finalVector = []
    for i in range(length):
        finalVector.append(0)

    for number in collumnNumbers:
        finalVector[number] = vector[collumnNumbers.index(number)]

    return finalVector

#Funkcja zwracająca maksymalną wartość funkcji celu i wektor dla którego jest ona osiągana
def printMaxVector(vectors, vectorC):
    isSet = False
    maxIndex = 0
    maxValue = 0
    for vector in vectors:
        value = 0
        for i in range(len(vector)):
            value = value + vector[i] * vectorC[i]
        if value > maxValue:
            isSet = True
            maxValue = value
            maxIndex = vectors.index(vector)

    if isSet:
        maxVector = vectors[maxIndex]
        print "Funkcja celu osiąga wartość maksymalną w wektorze: " + str(maxVector)
        print  "Maksymalna wartość funkcji celu = " + str(maxValue)
    else :
        print("Brak rozwiązań")


#Funkcja sprawdzająca, czy wektor rozwiązań ma tylko wartości nieujemne
def allPositive(vector):
    for value in vector:
        if value < 0:
            return False
    return True

#Program Główny:
#Poniżej należy wpisać dane programu liniowego w postaci normalnej:

matrixA = [[2, -2,-1,1,0],[-1,1,-3,0,1]]

vectorB = [4,-5]


vectorC = [3, -3, -2, 0, 0]
collumnsTemp = []
matrixesTemp = []

collumnsCombinations = []

matrixes = []
vectors = []

equationResults = []

finalResultVectors = []
#Szukamy wszystkich możliwych kombinacji kolumn, które dadząmacierze kwadratowe
for cols in itertools.combinations(range(len(matrixA[0])), len(matrixA)):
    collumnsTemp.append(cols)
    matrixesTemp.append(getMatrix(matrixA, cols))


#Rozpatrujemy tylko te macierze, które są nieosobliwe
i = 0

for matrix in matrixesTemp:
    if not isZero(matrix):
        collumnsCombinations.append(collumnsTemp[i])
        matrixes.append(matrix)
    i = i + 1

# Rozpatrujemy tylko nieujemne rozwiązania
for i in range(len(vectorB)):
    result = getResult(vectorB, matrixes[i])
    if allPositive(result):
        equationResults.append(result)


for equationResult in equationResults:
    finalResultVectors.append(
        getFinalVector(equationResult, collumnsCombinations[equationResults.index(equationResult)], len(vectorC)))

printMaxVector(finalResultVectors, vectorC)
