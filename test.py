#Ask user to set 4 digit pin number  and show them the pin number as output. 

while True:
    pin = input("Please enter a 4 digit pin number: ")

    if len(pin) != 4 or not pin.isdigit():
        print("Invalid pin number. Please try again.")
    else:
        print(f"Your pin number is: " + pin)
        break
