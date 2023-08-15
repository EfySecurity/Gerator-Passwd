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
    print("\033[1mBem-vindo ao Gerador de Senhas Fortes!\033[0m\n")

    length = int(input("\033[36mDigite o comprimento desejado da senha: \033[0m"))
    use_uppercase = input("\033[36mIncluir letras maiúsculas? (S/N): \033[0m").lower() == "s"
    use_digits = input("\033[36mIncluir dígitos? (S/N): \033[0m").lower() == "s"
    use_symbols = input("\033[36mIncluir símbolos? (S/N): \033[0m").lower() == "s"

    password = generate_strong_password(length, use_uppercase, use_digits, use_symbols)
    security_level = evaluate_password_security(password)

    print("\n\033[1mSenha Forte Gerada:\033[0m", password)
    print("\033[1mNível de Segurança:\033[0m", security_level, "de 5")

if __name__ == "__main__":
    main()
