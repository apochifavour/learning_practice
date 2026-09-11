try:
    age = int(input("Enter your age: "))
    print(f"you are {age} years old.")
except ValueError:
    print("That's not a valid number!")   

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(evens)

names = ["ada", "tunde", "chidi", "grace"]
uppercase_names = []
for name in names:
    uppercase_names.append(name.upper())

print(uppercase_names)