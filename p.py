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



#Inaczej:
 
def wartosc_f_celu(self, entering, leaving):
    self.enter(entering)
    self.leave(leaving)
    self.update
    return self.objective_value()

def co_wyrzucic(self, const_var):
    leaving_index = -1
    set_leaving = self.possible_leaving()
    objective_function = self.objective_value()
    for variable in set_leaving:
        f_celu = wartosc_f_celu(self, const_var, variable)
        if f_celu > objective_function:
            objective_function = f_celu
            leaving_index = set_leaving.index(variable)
    return set_leaving[leaving_index]

def maximal_objective_entering(self):
    print("max_obj")
    set_entering = self.possible_entering()
    set_leaving = self.possible_leaving()
    objective = self.objective_value()
    entering_index = -1
    for variable_enter in set_entering:
        print(variable_enter)
        leaving = co_wyrzucic(self, variable_enter)
        objective_for_variable = wartosc_f_celu(self, variable_enter, leaving)
        if objective_for_variable > objective:
            objective = objective_for_variable
            entering_index = set_entering.index(variable_enter)
    return set_entering[entering_index]
# Rozkład jednostajny
def uniform_entering(self):
    set = Set(self.possible_entering())
    return(set.random_element())

def uniform_leaving(self):
    set = Set(self.possible_leaving())
    return(set.random_element())


# minimalny index
def wypluj_nowy_dictionary(self, entering,leaving):
    self.enter(entering)
    self.leave(leaving)
    self.update
    return self

def minimal_index(self):
    entering_index = -1
    leaving_index = -1
    set_entering = self.possible_entering()
    set_leaving = self.possible_leaving()
    leaving_variable_index = 0
    for variable1 in set_entering:
        for variable2 in set_leaving:
            self = wypluj_nowy_dictionary(self, variable1,variable2)
            if self.is_dual_feasible() = "FALSE":
                entering_index = set_entering[variable1]
                leaving_index = set_leaving[variable2]
    return set_entering[entering_index]



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
