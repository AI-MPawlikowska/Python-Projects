

print("Welcome to the rollercoaster!")
try:
    height = int(input("What is your height in centimetres?\n"))
    bill = 0

    if height >= 120:
        print("You can ride the rollercoaster!")
        
        age = int(input("What is your age?\n"))
        
        if age <= 12:
            bill = 7
            print("Child tickets are $7.")
        elif age <= 18:
            bill = 10
            print("Youth tickets are $10.")
        else:
            bill = 15
            print("Adult tickets are $15.")
        
        extra_photo = input("Would you like to get a photo? YES or NO\n").strip().upper()
        
        if extra_photo == "YES":
            bill += 3
            print(f"You chose to add a photo. Your total is: ${bill}.")
        else:
            print(f"Thank you for the information. Your total is: ${bill}. Have a lot of fun!")
    
    else:
        print("Sorry, but you have to grow taller before you can ride. See you in the future!")
except ValueError:
    print("Invalid input. Please make sure to enter numbers where required.")
