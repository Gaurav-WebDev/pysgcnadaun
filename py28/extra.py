def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    return "Access granted"

try:
    print(check_age(26))
except ValueError as e:
    print("Error:", e)

