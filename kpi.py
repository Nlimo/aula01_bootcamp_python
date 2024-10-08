# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite seu salário: "))
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o bônus recebido: "))
# 4) Calcule o valor do bônus final
result = 1000 + salario * bonus
# 5) Imprima cálculo do KPI para o usuário
print(result)
# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f" {nome} seu salário com o bônus fica: {result}")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?