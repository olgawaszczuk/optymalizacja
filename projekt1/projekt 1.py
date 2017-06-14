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

# Punkt 2: Wybór zmiennej maksymalizującej wzrost funkcji celu
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
        new_self = deepcopy(self)
        get_possible_leaving(new_self, variable_enter)
        for variable_leave in get_possible_leaving(new_self, variable_enter):
            current_objective_function = get_new_dictionary(new_self, variable_enter, variable_leave).objective_value()
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
        new_self = deepcopy(self)
        for variable_leave in get_possible_leaving(new_self, variable_enter):
            current_objective_function = get_new_dictionary(new_self, variable_enter, variable_leave).objective_value()
            print variable_enter
            print variable_leave
            print ("obj funct:")
            print current_objective_function
            if current_objective_function > objective:
                leaving_index = set_leaving.index(variable_leave)
            print leaving_index
    return set_leaving[leaving_index]

# Zad 5: Wybór losowego elementu (prawdopodobieństwo jednostajne):
#wybór losowy zmiennej
def random_edge_entering(self):
	return list(self.possible_entering())[randrange(len(self.possible_entering()))]

def random_edge_leaving(self):
	return list(self.possible_leaving())[randrange(len(self.possible_leaving()))]

# Własne funkcje:
#minimal = 0
    for key in list_variables:
        temporary = list_variables[key]
        print("temp")
        print temporary
        if temporary > maximal:
            maximal = temporary
    print("temp")
    print temporary
