def generate_password(name: str, special_char: str, dob: str):
    name_parts = name.split()
    name = "".join(name_parts)[:5]  
    dob_sum = sum(int(digit) for digit in dob if digit.isdigit())
    while dob_sum >= 10:
        dob_sum = sum(int(digit) for digit in str(dob_sum))
    return name + special_char + str(dob_sum)
name = input("Enter your name : ")
special_char = input("Enter a special character: ")
dob = input("Enter your DOB (YYYYMMDD): ")
password = generate_password(name, special_char, dob)
print("Generated Password:", password)
