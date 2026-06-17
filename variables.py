#A variable is a name used to store data.

# ---------------- Strings ----------------
first_name = "Gagan"
last_name = "Nalla"
city = "Madurai"

print(first_name + " " + last_name)
print(f"{first_name} lives in {city}")

# ---------------- Integers ----------------
age = 22
experience = 3

print(f"Gagan is {age} years old")
print(f"Experience: {experience} years")

# ---------------- Float (decimal numbers) ----------------
salary = 25000.50
rating = 4.8

print(f"Salary is {salary}")
print(f"Rating is {rating}")

# ---------------- Boolean (True/False) ----------------
is_employee = True
is_manager = False

print(f"Is employee: {is_employee}")
print(f"Is manager: {is_manager}")

# ---------------- Multiple variables ----------------
a, b, c = 10, 20, 30
print(a, b, c)

# ---------------- Type checking ----------------
print(type(first_name))  # string
print(type(age))         # int
print(type(salary))      # float
print(type(is_employee)) # bool

# ---------------- Type conversion ----------------
age_str = str(age)
print("Age as string: " + age_str)

salary_int = int(salary)
print(f"Salary converted to int: {salary_int}")

# ---------------- Dynamic example ----------------
name = "Gagan"
score = 95

print(f"{name} scored {score} marks")



