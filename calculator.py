import os

def show_menu():
    print("Hier ist dein Taschenrechner!")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")
    print("5. Beenden")

def add(zahl1, zahl2):
    return zahl1 + zahl2

def subtract(zahl1, zahl2):
    return zahl1 - zahl2

def multiply(zahl1, zahl2):
    return zahl1 * zahl2

def divide(zahl1, zahl2):
    if zahl2 == 0:
        return "Division durch Null ist nicht erlaubt!"
    return zahl1 / zahl2

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        wahl = input("Bitte wähle eine Option (1-5): ")
        if wahl == '5':
            print("Taschenrechner wird beendet.")
            break
        try:
            zahl1 = float(input("Gib die erste Zahl ein: "))
            zahl2 = float(input("Gib die zweite Zahl ein: "))
        except ValueError:
            print("ungültige Eingabe! Bitte gib eine Zahl ein.")
            continue


        if wahl == '1':
            print("Ergebnis:", add(zahl1, zahl2)) 
        elif wahl == '2':
            print("Ergebnis:", subtract(zahl1, zahl2))
        elif wahl == '3':
            print("Ergebnis:", multiply(zahl1, zahl2))
        elif wahl == '4':
            result = divide(zahl1, zahl2)
            if isinstance(result, str):
                print(result)
            else:
                print("Ergebnis:", result)    

if __name__ == "__main__":
    main()
