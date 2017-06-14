W folderze „testy” dostępne są wykresy zestawiające  liczby kroków wykonywanych przez poszczególne alogrytmy przy rozwiązywaniu każdego z programów. W raporcie przedstawione zostaną wybrane z nich.

Wyniki testów przeprowadzonych kolejno dla każdej metody wyboru zmiennych jak i dla każdego problemu liniowego przedstawione są w tabeli "tabela_wyników". Tabela pokazuje ile kroków wykonał algorytm działający zgodnie z wybraną zasadą, przy rozwiązywaniu konkretnego przykładowego problemu. 

Widzimy, że problemy podzielić można na dwie kategorie: mało złożone i złożone.
W przypadku mało złożonych problemów takich, jak np. paint i furniture wszystkie reguły wyboru zmiennych mają zbliżoną efektywność, czyli znajdują optymalne rozwiązanie w 2-3 krokach. 

Na szczególną uwagę zasługują problemy, dla których algorytm musiał wykonać większą liczbę iteracji. W zależności od programu, różnice w efektywności metod były zasadnicze, lub znikome.

Gdy spojrzymy na wyniki dla problemów routes i profit możemy zauważyć, że każdy z algorytmów wykonał zbliżoną liczbę kroków, nie przekraczającą 8 kroków. Najlepiej poradziły sobie algorytmy largest_coefficient i max_bounds wykonując dla obu testów średnio 5 kroków. 

Zestawienie liczby kroków dla obu metod znajduje się na wykresach "profit" i "routes".

W przypadku problemu whiskas 2 metody dzielą się na dwie wyraźnie zróżnicowane grupy – metody które dobrze poradziły sobie z rozwiązaniem problemu (largest_coefficient i lexicographical_max, które znalazły optymalne rozwiązanie w 2 krokach) oraz pozostałe metody, które aby znaleźć optymalne rozwiązanie potrzebowały wykonać dużo więcej operacji.

Najcięższe do rozwiązania okazały się problemy hetmanów. Podczas gdy wszystkie pozostałe problemy liniowe rozwiązywane były w nie więcej niż 10-11 krokach, w przypadku problemu hetmanów, nawet małych (rozpatrywane były problemy dla szachownicy 3x3 i 5x5), do rozwiązania problemu potrzeba było co najmniej kilkunastu kroków. Nieodpowiednią do tego typu problemów okazała się szczególnie metoda maximal_objective_value, która przy problemie hetmani3 ( problem hetmanów dla szachownicy 3x3) potrzebowała aż 15 kroków (najwięcej wśród rozpatrywanych metod), natomiast dla problemu hetmanów5 nie zwróciła żadnej wartości (znajdowanie rozwiązania zostało zaniechane po ponad godzinie oczekiwania). 

Wnioski:
Metodą która najlepiej poradziła sobie z rozwiązaniem przykładowych problemów liniowych jest largest_coefficient. Jak widać w większości problemów w oparciu o tę regułę znaleźć można było rozwiązanie optymalne w najmniejszej liczbie kroków (lub zbliżonej do najmniejszej). Dodatkowo w przypadku problemu hetmanów i whiskas1 liczbę wykonywanych w ramach tej metody operacji była znacząco mniejsza niż przy większości pozostałych metod.
Dodatkowo średnia liczba kroków wykonanych przez metodę largest_coefficient we wszystkich testach operacji wyniosła 4,7 kroków, co jest najmniejszą średnią wartością kroków na cykl testów. 

