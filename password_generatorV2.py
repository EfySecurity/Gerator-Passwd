import random
import string

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class PasswordGenerator:
    def __init__(self):
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self, length=12):
        password = ''.join(random.choice(self.characters) for _ in range(length))
        return password

class PasswordEvaluator:
    @staticmethod
    def evaluate_security(password):
        security_score = 0

        if len(password) >= 12:
            security_score += 2
        elif len(password) >= 8:
            security_score += 1

        if any(c.isupper() for c in password) and any(c.islower() for c in password):
            security_score += 2

        if any(c.isdigit() for c in password):
            security_score += 1

        if any(c in string.punctuation for c in password):
            security_score += 1

        return security_score

def main():
    print(f"{Colors.HEADER}Bem-vindo ao Gerador de Senhas Fortes!{Colors.END}\n")

    length = int(input(f"{Colors.BLUE}Digite o comprimento desejado da senha: {Colors.END}"))
    
    generator = PasswordGenerator()
    evaluator = PasswordEvaluator()

    password = generator.generate_password(length)
    security_score = evaluator.evaluate_security(password)

    print(f"\n\033[1mSenha Forte Gerada:\033[0m {password}")
    print(f"\033[1mNível de Segurança:\033[0m {security_score} de 6")

if __name__ == "__main__":
    main()
