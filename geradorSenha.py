import random

def gerar_senha(length):
    """
    Gera uma senha aleatória.

    Retorna uma senha aleatória com o comprimento especificado.

    """
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
    senha = ''.join(random.choice(characters) for _ in range(length))
    return senha

def criptografar(info, shift):
    """
    Criptografa uma string utilizando a cifra de César.

    Retorna a string criptografada utilizando o deslocamento especificado.

    """
    encrypted_info = "".join(
        chr((ord(char) + shift - ord('a' if char.islower() else 'A')) % 26 + ord('a' if char.islower() else 'A'))
        if char.isalpha() else char for char in info)
    return encrypted_info

def armazenar_dados(service, username, senha):
    """
    Armazena os dados (nome do serviço, username e senha) em um dicionário.

    Se o serviço já estiver presente no dicionário, apenas atualiza o username.

    """
    encrypted_service = criptografar(service, 3)
    encrypted_username = criptografar(username, 3)
    encrypted_senha = criptografar(senha, 3)
    if encrypted_service not in database:
        database[encrypted_service] = {'username': encrypted_username, 'senha': encrypted_senha}
    else:
        print("Já existe um username para este serviço.")

def recuperar_dados(service, palavra_chave):
    """
    Recupera os dados (username e senha) de um serviço armazenado no dicionário.

    """
    if palavra_chave == "abra-te-sesamo":
        encrypted_service = criptografar(service, 3)
        if encrypted_service in database:
            decrypted_username = criptografar(database[encrypted_service]['username'], -3)
            decrypted_senha = criptografar(database[encrypted_service]['senha'], -3)
            print("Service:", service)
            print("Username:", decrypted_username)
            print("senha:", decrypted_senha)
        else:
            print("Não Encontrado. Tente Novamente")
    else:
        print("Palavra-chave Incorreta.")

# Dicionário para armazenar os dados
database = {}

def main():
    """
    Função principal do programa.
    """
    while True:
        print("\n1. Gerar senha")
        print("2. Consultar senha")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            service = input("Nome do serviço: ")
            username = input("Username: ")
            length = int(input("Comprimento da senha(quantidade de caracteres): "))
            senha = gerar_senha(length)
            armazenar_dados(service, username, senha)
            print("Senha gerada e armazenada com sucesso!")
        elif choice == '2':
            service = input("Nome do serviço para consultar: ")
            palavra_chave = input("Digite a palavra-chave: ")
            recuperar_dados(service, palavra_chave)
        elif choice == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()