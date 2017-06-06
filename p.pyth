# Maksymalna funkcja celu
def maximal_objective_entering(self):
    objective_value = self.objective_value
    for possible in self:
        self.enter(possible)
        self.update
        if self.objective_value() > objective_value:
            obejctive_value = self.objective_value()
            entering = possible
    return(entering)
