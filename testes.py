nome_do_usuario = input("digite seu nome: ").title()
senha_do_ususario = input("digite sua senha: ").title()

while(nome_do_usuario == senha_do_ususario):
        print("A senha não pode ser igual ao nome!")
        nome_do_usuario = input("digite seu nome: ").title()
        senha_do_ususario = input("digite sua senha: ").title()

print("usuário logado com sucesso!!!")

