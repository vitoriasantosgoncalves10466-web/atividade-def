Atividade 01
def controle_consumo_de_combustivel():
    nome = input("Nome do motorista:")

    km = float (input("Digite a quantidade de quilômetros percorridos:"))
    litros = float (input("Digite a quantidade de litros gastos:"))

    media = (km + litros)/ 3

    if media >= 15:
        situação = "Econômico"
    elif media  >= 10 and  media <= 14.9:
        situação = "Regular"
    else:
        situação = "Alto consumo"

    print(f"\nMotorista: {nome}")
    print(f"\nMédia: {media:.2f}")
    print(f"\nSituação: {situação}")

# controle_consumo_de_combustivel()

#Atividade 02
# def info():
#     nome = input ("Digite seu nome:")

#     peso = float(input("Digite seu peso em Kg: "))
#     altura = float(input("Digite sua altura em metros: "))
  
#     IMC = peso / (altura ** 2)

#     if IMC <=18.5:
#         situação = "Abaixo do peso"
#     elif IMC >= 18.5 and IMC <= 24.9:
#         situação = "Peso normal"
#     else:
#         situação = "Obesidade"

#     print(f"\nnome: {nome}")
#     print(f"\nIMC: {IMC:.2f}")
#     print(f"\nSituação: {situação}")

# info()

#Atividade 03
# def Verificador_de_Velocidade():
#     nome_motorista = input ("Digite o nome do motorista:")

#     km = float(input("Velocidade registrada em Km/h: "))

#     if km <= 80:
#         situação = "Dentro do limite"
#     elif km >= 81 and km <=100:
#         situação = "Leve"
#     else:
#         situação = "Grave!"

#     print(f"\nNome do motorista: {nome_motorista}")
#     print(f"\nSituação: {situação}")

# Verificador_de_Velocidade()

#Atividade 04

def operação(a, b):
    soma = a + b
    return soma 

resultado_soma = operação(9, 2)
print(resultado_soma)

