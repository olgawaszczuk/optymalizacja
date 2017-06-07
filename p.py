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
