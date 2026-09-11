user_name = input("Enter your first name: ")
birth_year_string = input("Enter your birth year (e.g., 2016): ")

currrent_year = 2026
user_age = currrent_year - int(birth_year_string)

clean_name = user_name.strip().title()
print(f"\nHello, {clean_name}! Based on your input, you turn {user_age} years old in {currrent_year}.")