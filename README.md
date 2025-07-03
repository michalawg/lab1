# Lab1

# Aplikacja To-Do List (Python CLI)
Prosta aplikacja konsolowa do zarządzania zadaniami.  
Pozwala dodawać zadania, wyświetlać listę oraz oznaczać zadania jako wykonane.

## Funkcje
- Dodawanie nowych zadań z terminem
- Wyświetlanie wszystkich zadań
- Oznaczanie zadania jako zakończone (po ID)
- Dane zapisywane lokalnie w pliku 'xwaz.txt'

## Przykład działania
== TODO LIST ==
[1] show tasks
[2] add task
[3] complete task
[4] exit

# Instalacja
Sklonuj repozytorium:

bash
git clone https://github.com/michalawg/lab1.git
cd lab1

# Licencja
Projekt dostępny na licencji MIT – szczegóły w pliku LICENSE

# Lab2 Zad2
Rozwiązywanie konfliktów:
- Utworzono 2 gałęzie z różnymi nagłówkami: feature/header-design-a, feature/header-design-b
- Połączenie feature/header-design-a z main przebiegło bez problemu
- Podczas łączenia feature/header-design-b wystąpił konflikt w pliku index.html
- Konflikt został ręcznie rozwiązany poprzez połączenie obu wersji nagłówków

# Lab2 Zad4-5
Dodano klasę `Calculator` z metodami:

- add(a, b) – dodawanie
- subtract(a, b) – odejmowanie
- multiply(a, b) – mnożenie
- divide(a, b) – dzielenie z obsługą dzielenia przez zero

Kod pokryty testami jednostkowymi z wykorzystaniem Pytest zgodnie z metodyką TDD.

# Lab2 Zad4
- Dodano nowy plik calculator.py z klasą Calculator
- Napisano testy jednostkowe dla funkcji dodawania, odejmowania, mnożenia, dzielenia i dzielenia przez zero
- Uzyskano 100% pokrycia testami
- Dodano testy integracyjne (osobne testy potwierdzające działanie pełnego kalkulatora)

# Lab2 Zad5
Utworzono gałąź kalkulator-funkcja
Zaimplementowano metodę power(a, b) z testem
Utworzono pull request i wykonano code review

"# Test commit" 

# Lab 3
# Deployment (CD)
Po wykonaniu push na branch main, automatycznie uruchamia się proces CD, który:
- Buduje obraz Dockera
- Zatrzymuje poprzedni kontener
- Uruchamia nowy kontener na porcie 80
- Wykonuje health check aplikacji
- W razie błędu przywraca poprzednią wersję kontenera (rollback)

Wymagania:
- runner self-hosted musi być uruchomiony (./run.sh)
- skonfigurowane sekrety SSH:
  - SSH_HOST
  - SSH_PORT
  - SSH_USER
  - SSH_PRIVATE_KEY
 
# CI/CD Workflow
## CI (testy, budowanie, lint)
Plik: .github/workflows/ci.yml
- Uruchamia się przy każdym push/pull request
- Sprawdza poprawność działania aplikacji
- (opcjonalnie) buduje obraz Docker

## CD (deploy na serwer)
Plik: .github/workflows/cd.yml
- Uruchamia się po push na main
- Wdraża aplikację na zdalnym serwerze

# Konfiguracja środowiska
- Runner działa na systemie Ubuntu 20.04
- Docker musi być zainstalowany
- Plik run.sh musi być uruchomiony w katalogu actions-runner

## Sekrety w GitHub
Ustawiono w repozytorium:
- SSH_HOST – adres IP/host zdalnej maszyny
- SSH_PORT – port SSH (domyślnie 22)
- SSH_USER – użytkownik SSH
- SSH_PRIVATE_KEY – klucz prywatny do połączenia SSH
