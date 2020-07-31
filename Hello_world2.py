name=input("what is your name?")
birth_year=(input("when were you born?"))

print(f"Hello, {name}")

from datetime import datetime
this_year = datetime.now().year

age = this_year-int(birth_year)

print(f"you must be {age}")
print(birth_year)
