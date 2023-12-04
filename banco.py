# Dados de login
login_correto = "pipoca"
senha_correta = "1609"

# Saldo inicial
saldo = 0

# Função para realizar o login
def fazer_login():
    login_digitado = input("Digite o login: ")
    senha_digitada = input("Digite a senha: ")

    if login_digitado == login_correto and senha_digitada == senha_correta:
        print(f"Logado na conta {login_correto}")
        return True
    else:
        print("Login ou senha incorretos. Encerrando o sistema.")
        return False

# Função para realizar depósito
def fazer_deposito():
    global saldo
    valor_deposito = float(input("Digite o valor do depósito: "))
    saldo += valor_deposito
    print(f"Depósito de ${valor_deposito} realizado com sucesso. Novo saldo: ${saldo}")

# Função para realizar saque
def fazer_saque():
    global saldo
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque > saldo:
        print("Saldo insuficiente. Saque não realizado.")
    else:
        saldo -= valor_saque
        print(f"Saque de ${valor_saque} realizado com sucesso. Novo saldo: ${saldo}")

# Função para exibir o saldo
def exibir_saldo():
    print(f"Saldo atual: ${saldo}")

# Função para a calculadora de investimento
def calculadora_investimento():
    investimento_total = float(input("Digite o valor do investimento: "))
    rentabilidade_mensal = float(input("Digite a rentabilidade mensal em %: "))

    retorno_mensal = (investimento_total * rentabilidade_mensal) / 100
    retorno_anual = retorno_mensal * 12
    total_investido = investimento_total + retorno_anual

    print(f"Retorno mensal $: {retorno_mensal}")
    print(f"Retorno anual $: {retorno_anual}")
    print(f"Total investido: {investimento_total} / Rentabilidade: {retorno_anual} / Total: {total_investido}")

# Loop principal
while True:
    if fazer_login():
        while True:
            # Menu de opções
            print("\nMenu:")
            print("1 - Depósito")
            print("2 - Saque")
            print("3 - Saldo")
            print("4 - Calculadora de investimento")
            print("5 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                fazer_deposito()
            elif opcao == "2":
                fazer_saque()
            elif opcao == "3":
                exibir_saldo()
            elif opcao == "4":
                calculadora_investimento()
            elif opcao == "5":
                print("Saindo do programa. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")
