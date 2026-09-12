print("=====barbearia=====")
def saudacao(mensagem):
    print("seja bem vindo á barbearia")
saudacao("mensagem")

print("""1 - Novo Agendamento
2 - Agendamentos Anteriores
3 - Deseja Sair?
""")

agendamentos = []
while True:
    try:
        escolha = int(input("Escolha: "))
        if escolha == 1:
            print("Novo Agendamento")
            nome_cliente = str(input("Qual o seu nome? "))
            serviço = str(input("Qual serviço Deseja? "))
            horario = str(input("Horario Desejado? "))
            dados_cliente = {
    "nome":  nome_cliente,
    "serviço": serviço,
    "horario": horario
}
            agendamentos.append(dados_cliente)  

        elif escolha == 2:
            print("Agendamentos Anteriores")
            for agendamento in agendamentos:
                print("nome:", agendamento["nome"])
                print("serviço:", agendamento["serviço"])
                print("horario:", agendamento["horario"])
                
        elif escolha == 3:
            print("Saindo...")
            break
    except ValueError:
        continue
    continuar = str(input("Deseja realizar um novo atendimento? S/N: ")).upper()
    if continuar == "N":
        print("Fim...")
        break
