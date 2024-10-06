# Print

print("I like pizza!")
print("It is really good.")
print("---")

# -----------------------------------------------------------------------------------------------------------------------

# Variables

## Ezek string típusok

first_name = "Kincső"
food = "pizza"
email = "kincso.csontos@gmail.com"

print(first_name)
print(f"Helló {first_name}!")
print(f"Te szereted a {food}t!")
print(f"A te email címed: {email}")

print("---")

## Ezek számtípusok

age = 20
quantity = 3
num_of_class = 30

print(f"Te {age} éves vagy")
print(f"{quantity} dolgot vettél")
print(f"Az osztályodban {num_of_class} tanuló van!")

print("---")

# float típusok

price = 10.99
gpa = 3.2
distance = 5.5

print(f"Az ára {price}")
print(f"A te gpa átlagod: {gpa}")
print(f"Te {distance}km-t futottál")
print("---")


# boolean

is_student = True

print(f"Te tanuló vagy? {is_student}")
print("---")

if is_student:
    print("Te tanuló vagy!")
else:
    print("Te nem vagy tanuló!")
print("---")


# -----------------------------------------------------------------------------------------------------------------------

name = "Doomhyena"
age = 20
gpa = 4.5
is_student = True


print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))
print("---")

age = float(age)
print(type(age))

age = str(age)

age += "1"

print(age)

name = bool(name)

print(name)
print("---")

name = input("What is your name? ")

print(f"Hello {name}")

