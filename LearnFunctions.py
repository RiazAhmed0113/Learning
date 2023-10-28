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






