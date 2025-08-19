import random
friends=["Alice", "Bob", "Charlie", "David", "Emanuel"]

who_pay=random.randint(0,4)
if who_pay == 0:
    print("Alice")

elif who_pay == 1:
    print("Bob")

elif who_pay == 2:
    print("Charlie")

elif who_pay == 3:
    print("David")

else:
    print("Emanuel")
