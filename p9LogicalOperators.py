# Logical operators (and, or, not) = used to check if two or more conditional statements are ture.

temp = float(input("What is the temperature outside? "))

if temp >= 0 and temp <= 30:    # both conditions have to be true
    print("The temperature is good")
elif temp < 0 or temp > 30:     # one condition has to be true
    print("Temperature is bad")

# if not(temp >= 0 and temp <= 30):     # flips/reverses/does the opposite
#    print("The temperature is good")
# elif not(temp < 0 or temp > 30):
#    print("Temperature is bad")
