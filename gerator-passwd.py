import random
import string

def generate_strong_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def evaluate_password_security(password):
    security_level = 0
    length = len(password)
    if length >= 8:
        security_level += 1
    if any(c.isdigit() for c in password):
        security_level += 1
    if any(c.isupper() for c in password):
        security_level += 1
    if any(c.islower() for c in password):
        security_level += 1
    if any(c in string.punctuation for c in password):
        security_level += 1
    
    return security_level

def main():
    print("Bem-vindo ao Gerador de Senhas Fortes!")

    length = int(input("Digite o comprimento desejado da senha: "))
    use_uppercase = input("Incluir letras maiúsculas? (S/N): ").lower() == "s"
    use_digits = input("Incluir dígitos? (S/N): ").lower() == "s"
    use_symbols = input("Incluir símbolos? (S/N): ").lower() == "s"

    password = generate_strong_password(length, use_uppercase, use_digits, use_symbols)
    security_level = evaluate_password_security(password)

    print("\nSenha Forte Gerada:", password)
    print("Nível de Segurança:", security_level, "de 5")

if __name__ == "__main__":
    main()
