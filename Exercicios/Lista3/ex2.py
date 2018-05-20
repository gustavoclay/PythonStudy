'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''
login = str(input("Login:"))
senha = str(input("senha:"))
while login == senha:
    print("login não pode ser igual a senha")
    login = str(input("Login:"))
    senha = str(input("senha:"))