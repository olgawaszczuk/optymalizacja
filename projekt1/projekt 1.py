#punkt 1: Wybór zmiennej o największym wspołczynniku funkcji celu

#dwie funkcje pomocnicze
#wybór zmiennych bazowych
def potencjalne_zmienne(ss, z):
	return list(ss.nonbasic_variables()).index(z)\

#wszystkie współczynniki w funkcji celu zmiennych wcześniej wybranych
def coef(ss, z):
    return ss.objective_coefficients()[potencjalne_zmienne(ss,z)]

# Wybór zmiennej o największym wspołczynniku funkcji celu
def largest_coefficient(self):
	return max(self.possible_entering(), key=(lambda x: coef(self, x) ) )

#dwie funkcje pomocnicze dla zmiennych wychodzących

#wybór zmiennych bazowych
def potencjalne_zmienne_b(ss, z):
	return list(ss.basic_variables()).index(z)

#wszystkie współczynniki w funkcji celu zmiennych wcześniej wybranych
def coef_b(ss, z):
    return ss.objective_coefficients()[potencjalne_zmienne_b(ss,z)]
# Wybór zmiennej o największym wspołczynniku funkcji celu
def largest_coefficient_leaving(self):
	return max(self.possible_leaving(), key=(lambda x: coef_b(self, x) ) )

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
            if current_objective_function > objective:
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
            if current_objective_function > objective:
                leaving_index = set_leaving.index(variable_leave)
            print leaving_index
    return set_leaving[leaving_index]
#Bland rule dla indeksu
def bland_rule_entering(self):
    print ("bland enter:")
    list_variables = {}
    set_entering = self.possible_entering()
    set_leaving = self.basic_variables()
    print set_entering
    for variable_enter in set_entering:
        new_self = deepcopy(self)
        for variable_leave in get_possible_leaving(new_self, variable_enter):
            new_self2 = get_new_dictionary(new_self, variable_enter, variable_leave)
            list_variables[variable_enter] = variable_leave
            if not new_self2.is_dual_feasible():
                """
                # list_variables[variable_enter] = variable_leave
                print ("zmienne entering:")
                print variable_enter
                print variable_leave
                print ("lista:")
                print list_variables
                print min(list_variables)
                """
    return min(list(list_variables))

def bland_rule_leaving(self, variable_enter):
    new_self = deepcopy(self)
    list_leaving = []
    for variable_leave in get_possible_leaving(new_self, variable_enter):
        new_self = get_new_dictionary(new_self, variable_enter, variable_leave)
        list_leaving.append(variable_leave)
        if not new_self.is_dual_feasible():
            """
            list_variables[variable_enter] = variable_leave
            print ("zmienne entering:")
            print variable_enter
            print variable_leave
            print ("lista:")
            print list_variables
            print ("min")
            print min(list_variables.values())
            """
    return min(list_leaving)
#Test:
def my_entering(self):
    print "Final entering: {}".format(bland_rule_entering(self))
    return bland_rule_entering(self)


def my_leaving(self):
    value_entering = bland_rule_entering(self)
    print "Final leaving: {}".format(bland_rule_leaving(self, value_entering))
    return bland_rule_leaving(self, value_entering)


def my_entering_lex(self):
    print "Final entering: {}".format(lexicographical_max_entering(self))
    return lexicographical_max_entering(self)
    # return bland_rule_entering(self)


def my_leaving_lex(self):
    print "Final leaving: {}".format(lexicographical_max_leaving(self))
    return lexicographical_max_leaving(self)
    # return bland_rule_leaving(self)





# Zad 5: Wybór losowego elementu (prawdopodobieństwo jednostajne):
#wybór losowy zmiennej
def random_edge_entering(self):
	return list(self.possible_entering())[randrange(len(self.possible_entering()))]

def random_edge_leaving(self):
	return list(self.possible_leaving())[randrange(len(self.possible_leaving()))]

# Własne funkcje:
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
