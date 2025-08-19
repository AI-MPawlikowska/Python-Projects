try:
    weight = float(input("Podaj swoją wagę w kilogramach:\n"))
    height = float(input("Podaj swój wzrost w metrach:\n "))

    if height > 2.5:
        print("Podany wzrost jest w innej jednostce aniżeli metr, zweryfikuj proszę podaną informację")
    else:
        bmi = weight / (height * height)
        print(f"Twoje BMI wynosi: {round(bmi, 2)}")

except ValueError:
    print("Podano niepoprawne dane. Proszę wprowadzić liczbę.")
