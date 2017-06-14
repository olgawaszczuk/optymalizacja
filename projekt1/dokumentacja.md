Projekt autorstwa: Olga Waszczuk, Małgorzata Łukomska

Całe podsumowanie projektu jest dostępne w pliku raport.pdf.

W pliku methods(pivot rules).py można znaleźć implementację następujących metod warunkujących wybór zmiennych wchodzących i wychodzących z programu liniowego (przy czym zachowałyśmy konwencję "nazwa_funkcji_entering" wybiera zmienną wchodzącą do programu, zaś "nazwa_funkcji_leaving" wybiera zmienną wychodzącą, bazując na zadanej regule) :
1) largest_coefficient: 
Funkcja wybieraja tę zmienną, przy której stoi największy współczynnik w funkcji celu.

2) maximal_objective:
Funkcja wybiera zmienną na podstawie wzorstu funkcji celu. Oznacza to, że funkcje maximal_objective_entering i maximal_objective_leaving zwracają dwie zmienne: wchodzącą i wychodzącą, tak, aby ich zamiana w programie dawała najwyższy wzrost funkcji celu spośród wszystkich możliwych par zmiennych wchodzących i wychodzących. Należy zauważyć, że zmienna wychodząca dobierana jest już do zmiennej wchodzącej.

3) bland_rule:
Funkcja bland_rule_entering zwraca zmienną wchodzącą o najniższym indeksie, zaś funkcja bland_rule_leaving dobiera do tej zmiennej możliwą zmienną wychodzącą, również na podstawie tego, aby jej index był najmniejszy w zbiorze możliwych zmiennych wychodzących.

4) random_edge:
Funkcja wybiera z prawdopodobieństwem jednostajnym losową zmienną, ze zmiennych, które mogą wejść lub wyjść z programu.

5) smallest_coefficient:
Funkcja zwraca zmienną, przy której w funkcji celu stoi najmniejszy współczynnik.

6) max_bounds_difference:
Porównujemy wartość bezwzględną różnicy współczynnika stojącego przy zmiennej w pierwszej funkcji ograniczającej, i sumy współczynników stojących przy zmiennej w pozostałych funkcjach ograniczających. Funkcja zwraca tę zmienną, dla której różnica ta jest największa.

7) lexicographical_min:
Funkcja zwraca najmniejszą zmienną wśród możliwych zmiennych wchodzących i wychodzących do programu, gdzie ułożenie zmiennych podlega pod porządek leksykograficzny.

8) lexicographical_max:
Funkcja zwraca największą zmienną wśród możliwych zmiennych wchodzących i wychodzących do programu, gdzie ułożenie zmiennych podlega pod porządek leksykograficzny.


W folderze "problems" znaleźć można 10 wybranych problemów liniowych, dla których przeprowadziłyśmy kolejno wybór zmiennych zgodnie z każdą z wymienionych powyżej metod.
W folderze "testy" zaprezentowane są wyniki wspomnianych testów i krótkie wnioski na temat metod wyboru zmiennych.


