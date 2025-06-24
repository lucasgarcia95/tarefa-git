#!/usr/bin/env python3

entrada_lista = input("Digite uma sequência de 04 números separados por espaço: ")
Num_listados = list(map(int, entrada_lista.split()))

if len(Num_listados) != 4:
    print("Por favor, insira exatamente 04 números!")
else:
    print("Números listados:", Num_listados)
    
    # Verificação par/ímpar
    for numero in Num_listados:
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")

    # Operações básicas
    soma = sum(Num_listados)
    subtracao = Num_listados[0]
    for n in Num_listados[1:]:
        subtracao -= n
    multiplicacao = 1
    for n in Num_listados:
        multiplicacao *= n
    try:
        divisao = Num_listados[0]
        for n in Num_listados[1:]:
            divisao /= n
    except ZeroDivisionError:
        divisao = "Erro: divisão por zero!"

    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")
