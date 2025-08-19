try:
        print("Welcome to the tip calculator\n" )
        bill=float(input("What was the total bill? $"))
        tip=int(input(f"How much percentage tip would you like to give? 10, 12 or 15? "))
        group= int(input("How many people to split the bill? "))

        tippay=float(bill*(tip/100)/group)

        print(f"Tip from each guest: {round(tippay,2)}$")
        topay=((bill/group)+tippay)
        total=print(f"Each person should pay total:{topay}$")
              

except ValueError:
    print("The data entered is incorrect. Please make sure you are entering numbers in decimal format.")
