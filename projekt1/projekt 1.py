#punkt 1: Wybór zmiennej o największym wspołczynniku funkcji celu

#dwie funkcje pomocnicze
#wybór zmiennych bazowych
def potencjalne_zmienne(ss, z):
	return list(ss.nonbasic_variables()).index(z)
#wszystkie współczynniki w funkcji celu zmiennych wcześniej wybranych
def coef(ss, z):
    return ss.objective_coefficients()[potencjalne_zmienne(ss,z)]
# Wybór zmiennej o największym wspołczynniku funkcji celu
def largest_coefficient(self):
	return max(self.possible_entering(), key=(lambda x: coef(self, x) ) )
