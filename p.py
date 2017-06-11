# Maksymalny współczynnik
def maximal_coefficient_entering(self):
    values = self.possible_entering()
    print "maximal_coefficient_entering:"
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

# Maksymalna funkcja celu
def maximal_objective_entering(self):
    set = self.possible_entering()
    objective_value = self.objective_value
    entering = 0
    for possible in set:
        self.enter(possible)
        self.update()
        if self.objective_value() > objective_value:
            obejctive_value = self.objective_value()
            entering = possible
    return(entering)

def maximal_objective_entering(self):
    set_entering = self.possible_entering()
    set_leaving=self.possible_leaving()
    objective_value = self.objective_value
    entering = 0
    leaving = 0
    for entering_variable in set_entering:
        for leaving_variable in set_leaving:
            self.enter(entering_variable)
            self.leave(leaving_variable)
            self.update()
            if self.objective_value() > objective_value:
                obejctive_value = self.objective_value()
                entering = entering_variable
                leaving = leaving_variable
    return(entering)

# Rozkład jednostajny
def uniform_entering(self):
    set = Set(self.possible_entering())
    return(set.random_element())

def uniform_leaving(self):
    set = Set(self.possible_leaving())
    return(set.random_element())

#Pomocnicze
self.objective_coefficients()
max(self.objective_coefficients())

set_entering = Set(self.possible_entering())
set_entering
set_entering.cardinality()

m =  matrix(set_entering.cardinality())
for i in range(set_entering.cardinality()):
        m[i] = i
        
    #######  
A = ([1, 1, 5], [3, 1, 0])
sage: b = (1000, 1500)
sage: c = (10, 5, 1)
sage: P = InteractiveLPProblem(A, b, c, variable_type=">=")
show(P)

P.constant_terms()

P = P.standard_form()
show(P)

self = P.initial_dictionary()
set = Set(self.possible_entering())
show(set)



show(self.objective_coefficients())
max(self.objective_coefficients())

self.objective_coefficients()
max(self.objective_coefficients())

set_entering = Set(self.possible_entering())
set_entering
set_entering.cardinality()

lista1 = list(self.possible_entering())
lista1
lista1[1]

lista2 = list(self.objective_coefficients())
lista2
lista2[1]
lista2.index(5)

lista1[lista2.index(max(lista2))]
