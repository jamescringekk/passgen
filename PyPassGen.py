import secrets
import string

def generate_password(length):
    # Defina os caracteres que serão usados na senha
    characters = string.ascii_letters + string.digits + string.punctuation

    # Gere a senha bibli secrets
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

# Solicite a quantidade desejada de caracteres
length_of_password = int(input("Lenght: "))

password = generate_password(length_of_password)

print("Generated pASS:", password)
