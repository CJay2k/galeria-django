1. Specyfikacja projektu
    1. Opis projektu
        1. Cel projektu
            * Projekt miał na celu stworzenie aplikacji internetowej umożliwiającej przechowywanie zdjęć/obrazów w bazie danych i wyświetlanie ich na witrynie internetowej.
        2. Zakres projektu
            * Utworzenie modelu bazy danych
            * Utworzenie widoków dla poszczególnych użytkowników i funkcji
            * Połączenie formularzy i funkcji z bazą danych
            
    2. Funkcjonalności
        • Dodawanie i usuwanie zdjęć/obrazów,
        • Rejestracja i logowanie,
        • Zmiana i przypomnienie hasła
        • Przeglądanie galerii innych użytkowników
        • Niezalogowany użytkownik nie może wejść na niektóre podstrony np. /add
        
    3. Użytkownicy aplikacji i ich uprawnienia
    
        * Administrator
            * Dostęp do panelu administracyjnego,
            * Dodawanie, usuwanie użytkowników,
            * Dodawanie, usuwanie do grupy superuser, 
            * Dodawanie, usuwanie zdjęć/obrazów z bazy danych

        * Użytkownik 
            * Logowanie
            * Dodawanie, usuwanie zdjęć/obrazów do swojego profilu
            * Zmiana, przypomnienie hasła
            * Przeglądanie galerii innych użytkowników, jeśli zna ich nazwy np. wpisując 127.0.0.1:8000/u/CJay można podglądnąć galeria użytkownika CJay
    4. Klienci aplikacji/systemu
        Osoby chcące przechować swoje obrazy na zewnętrznym serwerze, stworzyć własne galerie, zaprezentować swoje prace innym ludziom lub wykorzystać stronę, jako hosting obrazów.
2. Baza danych
    1. Diagram ERD
    
        ![Diagram ERD](https://raw.githubusercontent.com/CJay2k/galeria-django/master/dokumentacja/Diagram%20ERD.png)

3. Wykorzystane technologie/biblioteki
    * Django
        * Django-allauth
        * Django-crispy-forms
        * Django-currentuser
    * Python 
    * Pillow
    * HTML5
    * Javascript
    * CSS 
    * SQLite
4. Interfejs aplikacji
    ![Diagram ERD](https://raw.githubusercontent.com/CJay2k/galeria-django/master/dokumentacja/Interfejs.png)
    Zaraz po wejściu na stronę widzimy przykładowy album (jego właścicielem jest użytkownik: admin)

    ![Diagram ERD](https://raw.githubusercontent.com/CJay2k/galeria-django/master/dokumentacja/niezalogowany.png)
    Menu, które widzi niezalogowany użytkownik

    ![Diagram ERD](https://raw.githubusercontent.com/CJay2k/galeria-django/master/dokumentacja/zalogowany.png)
    Menu zalogowanego użytkownika

    ![Diagram ERD](https://raw.githubusercontent.com/CJay2k/galeria-django/master/dokumentacja/admin.png)
    Menu superusera



5. Jak uruchomić aplikację
    * Żeby uruchomić aplikację należy zainstalować Pythona w najnowszej wersji i dodać go do zmiennych środowiskowych abyśmy mogli używać polecenia python w każdym miejscu w systemie. Następnie należy otworzyć CMD i przejść do katalogu z projektem np.
        * cd „C:\Users\CJay\Desktop\galeria-django\”
    * Następnie wykonać polecenie: 
        * pip install -r requirements.txt

    * Jeśli wszystko przebiegło pomyślnie wystarczy  uruchomić serwer komendą:
        * python manage.py runserver

    * Teraz wystarczy wpisać adres w przeglądarkę http://127.0.0.1:8000.

6. Loginy i hasła
    1. Superuser: 
        * Login: admin
        * Hasło: admin
    2. Zwykły użytkownik
        * Login: CJay
        * Hasło: ZAQ!2wsx   
