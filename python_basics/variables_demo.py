#1. Creating variables of different types
player_name = "Sean"
age = 32
is_active = True
score = 95.5

#2. Checking types at runtime using type()
print("Initial values and types:")
print(player_name, "->", type(player_name))
print(age, "->", type(age))
print("-" * 30)

#3. Dynamic Typing
score = "Good"
print("After reassignment")
print(score, "->", type(score))

#4. Type Casting
org_value = "54"
converted_number = int(org_value)+ 3
print("After changing the type value is : " , converted_number)