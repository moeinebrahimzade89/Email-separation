from listemail import Domain, English_Name

email_details = []

email = input("email:")
if "@" in email:
    position = email.find("@")
    Username = email[:position]
    Domaine = email[position +1 :]
    email_type = Domaine
    for i in range(len(Domain)):
        if email_type == Domain[i]:
            email_type = English_Name[i]
    email_details.append({"Username": Username, "Domaine": Domaine, "email_type": email_type})
    for i, item in enumerate(email_details, start=1):
        print(f"{i} Username:{item['Username']} Domaine:{item['Domaine']} email_type:{item['email_type']}")
else:
    # If the entry does not have an @, it is not an email.
    print("Your email is incorrect.")
    
