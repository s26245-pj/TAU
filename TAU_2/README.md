1. **Skrypt testujący DuckDuckGo**
test_duckduckgo.py

Skrypt testuje funkcję wyszukiwania na stronie DuckDuckGo. Skrypt sprawdza, czy:

- Strona DuckDuckGo otwiera się poprawnie,
- Wyszukiwanie frazy "Best programming practices in Python" działa,
- Wyniki wyszukiwania zawierają odpowiednie elementy,
- Pierwszy wynik wyszukiwania zawiera słowo "Python" lub "Programming".
Kroki:

- Przejście na stronę DuckDuckGo.
- Sprawdzenie tytułu strony.
- Wpisanie frazy w pole wyszukiwania.
- Oczekiwanie na załadowanie wyników.
- Sprawdzenie tytułu wyników.
- Weryfikacja obecności wyników.
- Sprawdzenie treści pierwszego wyniku.
- Wydruk komunikatu o zakończeniu testu.
2. **Skrypt testujący Google** 
test_google.py

Skrypt testuje wyszukiwanie na Google, sprawdzając:

- Poprawność otwarcia strony Google,
- Wyszukiwanie frazy "Python automation testing",
- Obecność wyników wyszukiwania,
- Czy wyniki wyszukiwania zawierają frazę "Python".
Kroki:

- Przejście na stronę Google.
- Zaakceptowanie polityki prywatności (jeśli jest obecna).
- Sprawdzenie tytułu strony.
- Wpisanie frazy w pole wyszukiwania i potwierdzenie Enterem.
- Oczekiwanie na wyniki.
- Sprawdzenie tytułu wyników.
- Weryfikacja obecności wyników.
- Weryfikacja adresu URL pod kątem frazy "Python".
3. **Skrypt testujący Wikipedię**
test_wikipedia.py

Skrypt testuje wyszukiwanie i nawigację na stronie Wikipedii, sprawdzając:

- Poprawność otwarcia strony,
- Wyszukiwanie frazy "Python programming",
- Obecność sekcji z wynikami oraz poprawność linków wewnętrznych.
Kroki:

- Przejście na stronę Wikipedii.
- Sprawdzenie tytułu strony.
- Wpisanie frazy w pole wyszukiwania.
- Oczekiwanie na załadowanie artykułu.
- Sprawdzenie obecności słowa "language" w treści artykułu.
- Znalezienie pierwszego linku w artykule i kliknięcie go.
- Sprawdzenie tytułu nowej strony.
- Weryfikacja obecności słowa "syntax" na nowej stronie.
4. **Skrypt testujący Joinero**
test_joinero.py

Skrypt testuje proces wyszukiwania i dodawania produktu do koszyka w sklepie Joinero:

- Poprawność otwarcia strony,
- Funkcję wyszukiwania,
- Dodanie produktu do koszyka oraz aktualizację liczby produktów w koszyku.
Kroki:

- Przejście na stronę Joinero.
- Sprawdzenie tytułu strony.
- Wyszukanie produktu za pomocą pola wyszukiwania.
- Wpisanie litery "b" w polu wyszukiwania.
- Oczekiwanie na sugestie wyszukiwania.
- Wybranie pierwszej sugestii.
- Znalezienie i kliknięcie przycisku "Dodaj do koszyka".
- Sprawdzenie liczby produktów w koszyku.