# if statement = a block of code that will execute if it's condition is true

age = int(input("How old are you? "))

if age == 100:
    print("you are a century old")
elif age >= 18:
    print("You are an adult.")
elif age < 0:
    print("You are not born?...")
else:
    print("Child...")


