email = input("Digite seu email: ")
email2 = input("Digite outro email: ")

list_email = [email, email2]
check = "@jogajuntoinstituto.org"

for i in list_email:
    if check in i:
        print(f"Email {i} checado. Seu email faz parte do instituto!")
    else:
        print(f"Email {i} checado. Seu email não faz parte do instituto!")