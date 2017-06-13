#
# Rozne implementacje pivot rules


# Pkt1. Zmienna wchodząca o największym współczynniku
def maximal_coefficient_entering(self):
    values = self.possible_entering()
    max_coefficient = -99999999999
    max_coefficient_index = -1
    print values
    for value in values:
        print value
        print value.element()
        current_coefficient = value.coefficient({value: 1})
        if current_coefficient > max_coefficient:
            max_coefficient = current_coefficient
            max_coefficient_index = values.index(value)
    return values[max_coefficient_index]
    
    
#Opcja 2 ? Tu leaving nie działa
def maximal_coefficient_entering(self):
    variables = list(self.possible_entering())
    list_nonbasic = list(self.nonbasic_variables())
    print "maximal_coefficient_entering:"
    max_coefficient = -99999999999
    max_coefficient_index = -1
    print variables
    print self.objective_coefficients()
    print list_nonbasic
    for value in variables:
        print value
        print("index nonbasic:")
        print list_nonbasic.index(value)
        current_coefficient = self.objective_coefficients()[list_nonbasic.index(value)]
        print current_coefficient
        if current_coefficient > max_coefficient:
            max_coefficient = current_coefficient
            max_coefficient_index = variables.index(value)
            print("index:")
            print max_coefficient_index
    return variables[max_coefficient_index]  



def maximal_coefficient_leaving(self):
    values = self.possible_leaving()
    print "maximal_coefficient_leaving:"
    max_coefficient = -99999999999
    max_coefficient_index = -1
    print values
    for value in values:
        print value
        print value.element()
        current_coefficient = value.coefficient({value: 1})
        if current_coefficient > max_coefficient:
            max_coefficient = current_coefficient
            max_coefficient_index = values.index(value)
    return values[max_coefficient_index]

#Pkt 2. Zmienna maksymalizująca funkcję celu
def get_new_dictionary(self, entering, leaving):
    self.enter(entering)
    self.leave(leaving)
    self.update
    return self

def get_possible_leaving(self, entering):
    self.enter(entering)
    return list(self.possible_leaving())
    
     
def maximal_objective_entering(self):
    print("max_obj")
    set_entering = self.possible_entering()
    set_leaving = self.basic_variables()
    objective = self.objective_value()
    entering_index = -1
    print set_entering
    print set_leaving
    for variable_enter in set_entering:
        print("set:")
        get_possible_leaving(self, variable_enter)
        for variable_leave in get_possible_leaving(self, variable_enter):
            current_objective_function = get_new_dictionary(self, variable_enter, variable_leave).objective_value()
            print variable_enter
            print variable_leave
            print ("obj funct:")
            print current_objective_function
            entering_index = set_entering.index(variable_enter)
            print entering_index
    return set_entering[entering_index]

def maximal_objective_leaving(self):
    print("max_obj")
    set_entering = self.possible_entering()
    set_leaving = self.basic_variables()
    objective = self.objective_value()
    entering_index = -1
    print set_entering
    print set_leaving
    for variable_enter in set_entering:
        for variable_leave in get_possible_leaving(self, variable_enter):
            current_objective_function = get_new_dictionary(self, variable_enter, variable_leave).objective_value()
            print variable_enter
            print variable_leave
            print ("obj funct:")
            print current_objective_function
            leaving_index = set_leaving.index(variable_leave)
            print leaving_index
    return set_leaving[leaving_index]
    
# zad 4 Bland'd Rule (wybieramy zmienną o najmniejszym indeksie której reduced cost jest ujemny, tzn problem dualny nie jest feasible)
def bland_rule_entering(self):
    print ("max index:")
    list_variables = {}
    set_entering = self.possible_entering()
    set_leaving = self.basic_variables()
    print set_entering
    for variable_enter in set_entering:
        for variable_leave in get_possible_leaving(self, variable_enter):
            new_self = get_new_dictionary(self, variable_enter, variable_leave)
            if not new_self.is_dual_feasible():
                list_variables[variable_enter] = variable_enter
                print ("zmienne entering:")
                print variable_enter
                print variable_leave
                print ("lista:")
                print list_variables
                print min(list_variables)
    return min(list(list_variables))

def bland_rule_leaving(self):
    print ("min index:")
    list_variables = {}
    set_entering = self.possible_entering()
    set_leaving = self.basic_variables()
    for variable_enter in set_entering:
        for variable_leave in get_possible_leaving(self, variable_enter):
            new_self = get_new_dictionary(self, variable_enter, variable_leave)
            if not new_self.is_dual_feasible():
                list_variables[variable_enter] = variable_leave
                print ("zmienne entering:")
                print variable_enter
                print variable_leave
                print ("lista:")
                print list_variables
                print min(list_variables)
    return min(list(list_variables))


# Funkcje własne:
#Wybór losowego elementu ze zbioru
def random_entering(self):
    set = Set(self.possible_entering())
    return(set.random_element())

def random_leaving(self):
    set = Set(self.possible_leaving())
return(set.random_element())

#Wybór elementu o największej różnicy współczynników w ograniczeniach 
def max_bounds_difference_entering(self):
    print("max bound:")
    variables = self.possible_entering()
    list_of_differences = {}
    print (variables)
    for variable in variables:
        print variable
        list_of_coefficients = self.column_coefficients(variable)
        difference = 0
        for i in range(len(list_of_coefficients)):
            difference = abs(difference - list_of_coefficients[i])
        list_of_differences[variable] = difference
        print ("list of diff:")
        print list_of_differences
        maximal = 0
        key_maximal = 0
        for key in list_of_differences:
            temporary = list_of_differences[key]
            print ("temporary:")
            print key_maximal          
            print temporary
            if temporary > maximal:
                maximal = temporary
                key_maximal = key
        print("max enter:")
        print maximal
        print key_maximal
        print variables.index(key_maximal)
    return key_maximal

#Uwaga column_coefficients(variable) działa tylko dla nonbasic variables. Na leaving jakoś inaczej metodę
def max_bounds_difference_leaving(self):
    print("max bound:")
    variables = self.possible_leaving()
    list_of_differences = {}
    print (variables)
    for variable in variables:
        print variable
        list_of_coefficients = self.column_coefficients(variable)
        print list_of_coefficients
        difference = 0
        for i in range(len(list_of_coefficients)):
            difference = abs(difference - list_of_coefficients[i])
        list_of_differences[variable] = difference
        print ("list of diff:")
        print list_of_differences
        maximal = 0
        key_maximal = 0
        for key in list_of_differences:
            temporary = list_of_differences[key]
            print ("temporary:")
            print key_maximal          
            print temporary
            if temporary > maximal:
                maximal = temporary
                key_maximal = key
        print("max:")
        print maximal
        print key_maximal
    return key_maximal
        

       



#Porzadek leksykograficzny, minimum

def lexicographical_min_entering(self):
    return min(self.possible_entering())


def lexicographical_min_leaving(self):
    return min(self.possible_leaving())


# Porzadek leksykograficzny, maximum

def lexicographical_max_entering(self):
    return max(self.possible_entering())


def lexicographical_max_leaving(self):
    return max(self.possible_leaving())


#
# Wybor funkcji pivot
#

def my_entering(self):
    return maximal_coefficient_entering(self)


def my_leaving(self):
    return maximal_coefficient_leaving(self)


#
# Definicja problemu
#

LP = \
    """
    Minimize
    Total_Cost_of_Ingredients_per_can: 0.008 Ingr_BEEF + 0.013 Ingr_CHICKEN
     + 0.001 Ingr_GEL + 0.01 Ingr_MUTTON + 0.002 Ingr_RICE + 0.005 Ingr_WHEAT
    Subject To
    FatRequirement: 0.1 Ingr_BEEF + 0.08 Ingr_CHICKEN + 0.11 Ingr_MUTTON
     + 0.01 Ingr_RICE + 0.01 Ingr_WHEAT >= 6
    FibreRequirement: 0.005 Ingr_BEEF + 0.001 Ingr_CHICKEN + 0.003 Ingr_MUTTON
     + 0.1 Ingr_RICE + 0.15 Ingr_WHEAT <= 2
    PercentagesSum: Ingr_BEEF + Ingr_CHICKEN + Ingr_GEL + Ingr_MUTTON + Ingr_RICE
     + Ingr_WHEAT = 100
    ProteinRequirement: 0.2 Ingr_BEEF + 0.1 Ingr_CHICKEN + 0.15 Ingr_MUTTON
     + 0.04 Ingr_WHEAT >= 8
    SaltRequirement: 0.005 Ingr_BEEF + 0.002 Ingr_CHICKEN + 0.007 Ingr_MUTTON
     + 0.002 Ingr_RICE + 0.008 Ingr_WHEAT <= 0.4
    End
    """

from sage.misc.html import HtmlFragment
import types


def my_run_simplex_method(self):
    output = []
    while not self.is_optimal():
        self.pivots += 1
        if self.entering() is None:
            self.enter(self.pivot_select_entering())
        if self.leaving() is None:
            if self.possible_leaving():
                self.leave(self.pivot_select_leaving())

        output.append(self._html_())
        if self.leaving() is None:
            output.append("The problem is unbounded in $()$ direction.".format(latex(self.entering())))
            break
        output.append(self._preupdate_output("primal"))
        self.update()
    if self.is_optimal():
        output.append(self._html_())
    return HtmlFragment("\n".join(output))


#
# Parsowanie danych
#

class Matrix:
    """ output matrix class """

    class Objective:
        def __init__(self, expression, sense, name):
            if name:
                self.name = name[int(0)]
            else:
                self.name = ""
            self.sense = sense  # 1 is minimise, -1 is maximise
            self.expression = expression  # a dict with variable names as keys, and coefficients as values

    class Constraint:
        def __init__(self, expression, sense, rhs, name):
            if name:
                self.name = name[int(0)]
            else:
                self.name = ""
            self.sense = sense  # 1 is geq, 0 is eq, -1 is leq
            self.rhs = rhs
            self.expression = expression

    class Variable:
        def __init__(self, bounds, category, name):
            self.name = name
            self.bounds = (bounds["lb"], bounds["ub"])  # a tuple (lb, ub)
            self.category = category  # 1 for int, 0 for linear

    def __init__(self, parserObjective, parserConstraints, parserBounds, parserGenerals, parserBinaries):

        self.objective = Matrix.Objective(varExprToDict(parserObjective.varExpr), objSenses[parserObjective.objSense],
                                          parserObjective.name)

        self.constraints = [Matrix.Constraint(varExprToDict(c.varExpr), constraintSenses[c.sense], c.rhs, c.name) for c
                            in parserConstraints]

        boundDict = getBoundDict(parserBounds,
                                 parserBinaries)  # can't get parser to generate this dict because one var can have several bound statements

        allVarNames = set()
        allVarNames.update(self.objective.expression.keys())
        for c in self.constraints:
            allVarNames.update(c.expression.keys())
        allVarNames.update(parserGenerals)
        allVarNames.update(boundDict.keys())

        self.variables = [
            Matrix.Variable(boundDict[vName], ((vName in list(parserGenerals)) or (vName in list(parserBinaries))),
                            vName) for vName in allVarNames]

    def __repr__(self):
        return "Objective%s\n\nConstraints (%d)%s\n\nVariables (%d)%s" \
               % ("\n%s %s %s" % (self.objective.sense, self.objective.name, str(self.objective.expression)), \
                  len(self.constraints), \
                  "".join(
                      ["\n(%s, %s, %s, %s)" % (c.name, str(c.expression), c.sense, c.rhs) for c in self.constraints]), \
                  len(self.variables), \
                  "".join(["\n(%s, %s, %s)" % (v.name, str(v.bounds), v.category) for v in self.variables]))

    def getInteractiveLPProblem(self):
        A = [[0 for x in range(len(self.variables))] for y in range(len(self.constraints))]
        b = [0] * len(self.constraints)
        c = [0] * len(self.variables)

        for i, constraint in enumerate(self.constraints):
            for v, a in constraint.expression.iteritems():
                if constraint.sense == 1:
                    A[i][map(lambda x: x.name, self.variables).index(v)] = -a
                else:
                    A[i][map(lambda x: x.name, self.variables).index(v)] = a

                if constraint.sense == 1:
                    b[i] = -constraint.rhs
                else:
                    b[i] = constraint.rhs

        for v, a in self.objective.expression.iteritems():
            if self.objective.sense == 1:
                c[map(lambda x: x.name, self.variables).index(v)] = -a
            else:
                c[map(lambda x: x.name, self.variables).index(v)] = a

        AA = ()
        bb = ()
        cc = ()

        for a in A:
            aaa = []
            for aa in a:
                aaa.append(aa * int(10000))
            AA = AA + (list(aaa),)
        for b in b:
            bb = bb + (b * int(10000),)
        for c in c:
            cc = cc + (c * int(10000),)

        lpp = InteractiveLPProblemStandardForm(AA, bb, cc)

        for i, v in enumerate(self.variables):
            if v.bounds[int(1)] < infinity:
                coef = [0, ] * len(self.variables)
                coef[i] = 1
                lpp = lpp.add_constraint((coef), v.bounds[int(1)] * int(10000))
            if v.bounds[int(0)] > -infinity:
                coef = [0, ] * len(self.variables)
                coef[i] = -1
                lpp = lpp.add_constraint((coef), -v.bounds[int(0)] * int(10000))

        return lpp


def varExprToDict(varExpr):
    return dict((v.name[int(0)], v.coef) for v in varExpr)


def getBoundDict(parserBounds, parserBinaries):
    boundDict = defaultdict(lambda: {"lb": -infinity,
                                     "ub": infinity})  # need this versatility because the lb and ub can come in separate bound statements

    for b in parserBounds:
        bName = b.name[int(0)]

        # if b.free, default is fine

        if b.leftbound:
            if constraintSenses[b.leftbound.sense] >= 0:  # NUM >= var
                boundDict[bName]["ub"] = b.leftbound.numberOrInf

            if constraintSenses[b.leftbound.sense] <= 0:  # NUM <= var
                boundDict[bName]["lb"] = b.leftbound.numberOrInf

        if b.rightbound:
            if constraintSenses[b.rightbound.sense] >= 0:  # var >= NUM
                boundDict[bName]["lb"] = b.rightbound.numberOrInf

            if constraintSenses[b.rightbound.sense] <= 0:  # var <= NUM
                boundDict[bName]["ub"] = b.rightbound.numberOrInf

    for bName in parserBinaries:
        boundDict[bName]["lb"] = 0
        boundDict[bName]["ub"] = 1

    return boundDict


def multiRemove(baseString, removables):
    """ replaces an iterable of strings in removables
        if removables is a string, each character is removed """
    for r in removables:
        try:
            baseString = baseString.replace(r, "")
        except TypeError:
            raise TypeError, "Removables contains a non-string element"
    return baseString


from pyparsing import *
from sys import argv, exit
from collections import defaultdict

MINIMIZE = 1
MAXIMIZE = -1

objSenses = {"max": MAXIMIZE, "maximum": MAXIMIZE, "maximize": MAXIMIZE, \
             "min": MINIMIZE, "minimum": MINIMIZE, "minimize": MINIMIZE}

GEQ = 1
EQ = 0
LEQ = -1

constraintSenses = {"<": LEQ, "<=": LEQ, "=<": LEQ, \
                    "=": EQ, \
                    ">": GEQ, ">=": GEQ, "=>": GEQ}

infinity = 1E30


def read(fullDataString):
    # name char ranges for objective, constraint or variable
    allNameChars = alphanums + "!\"#$%&()/,.;?@_'`{}|~"
    firstChar = multiRemove(allNameChars, nums + "eE.")  # <- can probably use CharsNotIn instead
    name = Word(firstChar, allNameChars, max=255)
    keywords = ["inf", "infinity", "max", "maximum", "maximize", "min", "minimum", "minimize", "s.t.", "st", "bound",
                "bounds", "bin", "binaries", "binary", "gen", "general", "end"]
    pyKeyword = MatchFirst(map(CaselessKeyword, keywords))
    validName = ~pyKeyword + name
    validName = validName.setResultsName("name")

    colon = Suppress(oneOf(": ::"))
    plusMinus = oneOf("+ -")
    inf = oneOf("inf infinity", caseless=True)
    number = Word(nums + ".")
    sense = oneOf("< <= =< = > >= =>").setResultsName("sense")

    # section tags
    objTagMax = oneOf("max maximum maximize", caseless=True)
    objTagMin = oneOf("min minimum minimize", caseless=True)
    objTag = (objTagMax | objTagMin).setResultsName("objSense")

    constraintsTag = oneOf(["subj to", "subject to", "s.t.", "st"], caseless=True)

    boundsTag = oneOf("bound bounds", caseless=True)
    binTag = oneOf("bin binaries binary", caseless=True)
    genTag = oneOf("gen general", caseless=True)

    endTag = CaselessLiteral("end")

    # coefficient on a variable (includes sign)
    firstVarCoef = Optional(plusMinus, "+") + Optional(number, "1")
    firstVarCoef.setParseAction(
        lambda tokens: eval("".join(tokens)))  # TODO: can't this just be eval(tokens[0] + tokens[1])?

    coef = plusMinus + Optional(number, "1")
    coef.setParseAction(lambda tokens: eval("".join(tokens)))  # TODO: can't this just be eval(tokens[0] + tokens[1])?

    # variable (coefficient and name)
    firstVar = Group(firstVarCoef.setResultsName("coef") + validName)
    var = Group(coef.setResultsName("coef") + validName)

    # expression
    varExpr = firstVar + ZeroOrMore(var)
    varExpr = varExpr.setResultsName("varExpr")

    # objective
    objective = objTag + Optional(validName + colon) + varExpr
    objective = objective.setResultsName("objective")

    # constraint rhs
    rhs = Optional(plusMinus, "+") + number
    rhs = rhs.setResultsName("rhs")
    rhs.setParseAction(lambda tokens: eval("".join(tokens)))

    # constraints
    constraint = Group(Optional(validName + colon) + varExpr + sense + rhs)
    constraints = ZeroOrMore(constraint)
    constraints = constraints.setResultsName("constraints")

    # bounds
    signedInf = (plusMinus + inf).setParseAction(lambda tokens: (tokens[int(0)] == "+") * infinity)
    signedNumber = (Optional(plusMinus, "+") + number).setParseAction(lambda tokens: eval(
        "".join(tokens)))  # this is different to previous, because "number" is mandatory not optional
    numberOrInf = (signedNumber | signedInf).setResultsName("numberOrInf")
    ineq = numberOrInf & sense
    sensestmt = Group(
        Optional(ineq).setResultsName("leftbound") + validName + Optional(ineq).setResultsName("rightbound"))
    freeVar = Group(validName + Literal("free"))

    boundstmt = freeVar | sensestmt
    bounds = boundsTag + ZeroOrMore(boundstmt).setResultsName("bounds")

    # generals
    generals = genTag + ZeroOrMore(validName).setResultsName("generals")

    # binaries
    binaries = binTag + ZeroOrMore(validName).setResultsName("binaries")

    varInfo = ZeroOrMore(bounds | generals | binaries)

    grammar = objective + constraintsTag + constraints + varInfo + endTag

    # commenting
    commentStyle = Literal("\\") + restOfLine
    grammar.ignore(commentStyle)

    # parse input string
    parseOutput = grammar.parseString(fullDataString)

    # create generic output Matrix object
    m = Matrix(parseOutput.objective, parseOutput.constraints, parseOutput.bounds, parseOutput.generals,
               parseOutput.binaries)

    return m


#
# Parsowanie danych
#

m = read(LP)
P = m.getInteractiveLPProblem()

#
# Ustawienie wlasnej funkcji pivot
#

D = P.initial_dictionary()

if not D.is_feasible():
    print "The initial dictionary is infeasible, solving auxiliary problem."
    # Phase I
    AD = P.auxiliary_problem().initial_dictionary()
    AD.enter(P.auxiliary_variable())
    AD.leave(min(zip(AD.constant_terms(), AD.basic_variables()))[int(1)])
    AD.run_simplex_method()
    if AD.objective_value() < 0:
        print "The original problem is infeasible."
        P._final_dictionary = AD
    else:
        print "Back to the original problem."
        D = P.feasible_dictionary(AD)

D.run_simplex_method = types.MethodType(my_run_simplex_method, D)
D.pivots = 0

D.pivot_select_entering = types.MethodType(my_entering, D)
D.pivot_select_leaving = types.MethodType(my_leaving, D)

#
# Algorytm sympleks
#

if D.is_feasible():
    D.run_simplex_method()

print "Number of pivot steps: ", D.pivots

print D.objective_value()
print P.optimal_solution()
# print maximal_coefficient_entering(D)
