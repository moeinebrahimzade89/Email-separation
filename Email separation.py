email = input("email:")
if "@" in email:
    position = email.find("@")
    print(f"Username:{email[:position]}")
    print(f"Domain:{email[position +1 :]}")
else:
    # If the entry does not have an @, it is not an email.
    print("Your email is incorrect.")
