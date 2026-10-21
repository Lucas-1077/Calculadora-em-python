def somar():
    lista = []
    texto = []
    qta = int(input("\nQuantos numeros quer somar? "))

    while len(lista) < qta:
        numero = int(input("Número "))
        lista.append(numero)
        variavel = str(numero)
        texto.append(variavel)

    print("\nO resultado da soma é", sum(lista))
    historico.append(f'{" + ".join(texto)} = {sum(lista)}')
    analise.append(sum(lista))


def subtrair():
    lista = []
    texto = []
    qta = int(input("\nQuantos numeros quer subtrair? "))

    while len(lista) < qta:
        numero = int(input("Número "))
        lista.append(numero)
        variavel = str(numero)
        texto.append(variavel)
        sub = lista[0]

    for i in lista[1:]:
        sub -= i

    print("\nO resultado da subtração é", sub)
    historico.append(f'{" - ".join(texto)} = {sub}')
    analise.append(sub)


def dividir():
    print("\nQual número quer dividir?")
    a = int(input("Número "))
    print("Por qual?")
    b = int(input("Número "))
    print("\nO resultado da divisão é", round(a / b, 2))

    historico.append(f"{a} / {b} = {round(a / b, 2)}")
    analise.append(round(a / b, 2))


def multiplicar():
    print("\nQual número quer multiplicar?")
    a = int(input("Número "))
    print("Por qual?")
    b = int(input("Número "))
    print("\nO resultado da multiplicação é", round(a * b, 2))

    historico.append(f"{a} * {b} = {round(a * b, 2)}")
    analise.append(round(a * b, 2))


historico = []
analise = []

while True:
    print("\nOlá, seja bem vindo a nossa calculadora py")
    print("-------------  O que deseja --------------\n")
    print("1 - calcular\n2 - ver historico\n3 - ver análise")
    info = input("Digite aqui ")

    if info == "1" or info == "calcular":
        print("\nQual operação você deseja? ")
        print("1 - Somar \n2 - Subtrair \n3 - Dividir \n4 - Multiplicar")
        operacao = input()

        if operacao == str("Somar").lower() or operacao == "1":
            somar()

        elif operacao == str("Subtrair").lower() or operacao == "2":
            subtrair()

        elif operacao == str("Dividir").lower() or operacao == "3":
            dividir()

        elif operacao == str("Multiplicar").lower() or operacao == "4":
            multiplicar()

        else:
            print("\nNúmero digitado inválido, digite outro")

    elif info == "2" or info == "ver historico":

        print("\nVeja seu historico")

        for i in historico:
            print(i)

    elif info == "3" or info == "ver análise":
        print(sum(analise) / len(analise))
