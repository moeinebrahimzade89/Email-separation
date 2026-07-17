from listemail import Domain, English_Name

email_details = []

email = input("email: ")
if "@" in email:
    f = open("Save_email.txt", "a")
    f.write(email + "\n")
    f.close()
    position = email.find("@")
    username = email[:position]
    domaine = email[position + 1:]
    email_type = domaine
    for i in range(len(Domain)):
        if email_type == Domain[i]:
            email_type = English_Name[i]
    email_details.append(
        {"username": username, "domaine": domaine, "email_type": email_type}
    )
    for i, item in enumerate(email_details, start=1):
        print(
            f"{i} Username:{item['username']} Domaine:{item['domaine']} "
            f"email_type:{item['email_type']}"
        )
else:
    # If the entry does not have an @, it is not an email.
    print("Your email is incorrect.")

