
user_input = input ("Enter  your Age")
esValido=False

while(esValido==False):
    try:
        val = int(user_input)
        print("Yes input string is an Integer.")
        print("Input number value is: ", val)
        esValido=True
    except ValueError:
        print("That's not an int!")
        print("No.. input string is not an Integer. It's a string")
        user_input = input("Enter  your Age")
