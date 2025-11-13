punkty = float(input("Podaj punkty: "))

if punkty > 80:
    print("Zaliczyłeś egzamin, gratuluję!")
elif punkty >= 50 and punkty <= 80:
    print("Zaliczyłeś egzamin, ale możesz poprawić jego wynik!")
else:
    print("Nie zaliczyłeś egzaminu, pozdro na poprawce!")
