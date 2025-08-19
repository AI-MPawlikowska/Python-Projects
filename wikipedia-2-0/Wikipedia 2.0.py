"""Program do dodawania, usuwania i znajdowania definicji. Wikipedia 2.0"""

definicje={}
while(True):
    print("Witaj oto program, w którym zbudujesz swój prywatny słownik\n jesteś gotowy na to wyzwanie?")

    print("""
                    .-~~~~~~~~~-._       _.-~~~~~~~~~-.
                __.'              ~.   .~              `.__
              .'//                  \./                  \\`.
            .'//                     |                     \\`.
          .'// .-~"""""""~~~~-._     |     _,-~~~~"""""""~-. \\`.     
        .'//.-"                 `-.  |  .-'                 "-.\\`.
      .'//______.============-..   \ | /   ..-============.______\\`.
    .'______________________________\|/______________________________`.
    """)
    
    print("1: Dodaj definicję.")
    print("2: Znajdź definicję.")
    print("3: Usuń definicję.")
    print("4: Zakończ program.")

    wybor=input("Co chcesz zrobić? ")


    if wybor == "1":
        klucz = input ("Podaj klucz (słowo) do zdefiniowania:  ")
        definicja= input("Podaj definicję: ")
        definicje[klucz]=definicja
        print("Definicja dodana pomyślnie.")

    elif  wybor == "2":
        klucz = input("Podaj klucz (słowo), które chcesz znaleźć:  ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
                print("Nie znaleziono definicji o nazwie", klucz)
                
    elif(wybor =="3"):
        klucz = input("Podaj klucz (słowo), które chcesz usunąć:  ")
        if klucz in definicje:
            del (definicje[klucz])
            print("Usunieto definicje o nazwie", klucz)
        else:
                print("Nie znaleziono definicji o nazwie", klucz)

    elif wybor == "4":
        print("Program zakończony.")
        break
else:
    print("Podałeś hasło z poza słownika.")
