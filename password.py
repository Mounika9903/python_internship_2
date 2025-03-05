def generate_password(name, special_char,dob ):
    
    dob_sum = sum(int(digit) for digit in dob if digit.isdigit())
    
    while dob_sum >= 10:
        dob_sum = sum(int(digit) for digit in str(dob_sum))
    
    return name + special_char +str(dob_sum)

name = input("Enter your name (at least 5 characters): ")
special_char = input("Enter a special character: ")
dob = input("Enter your DOB (YYYYMMDD): ")

password = generate_password(name, special_char,dob)
print("Generated Password:", password)