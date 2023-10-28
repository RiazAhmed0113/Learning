# function = a block of reusable code
#            place () after the function name to invoke it.

def happy_function(name, age):      # orders of parameters matter
    print(f"Happy Birthday to {name}!!!")
    print(f"You are {age} years old!")
    print("Happy Birthday to You!")

happy_function("Riaz", 18)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of £{amount:.2f} is due: {due_date}")

display_invoice("Riaz", 500, "1/11")


# return = statement used to end a function and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))

def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + " " + last_name

full_name = create_name("riaz", "ahmed")
print(full_name)


