email = input("email: ")

if "@" in email:
    position = email.find("@")
    print(f"Username: {email[:position]}")
    print(f"Domain: {email[position + 1:]}")
else:
    print("Your email is incorrect.")
