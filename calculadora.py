#!/usr/bin/env python3
entrada_lista = input("Digite uma sequência de 04 números: ")
Num_listados = list(map(int, entrada_lista.split()))
if len(Num_listados) != 4:
    print("Por favor, insira exatamente 04 números!")
else:
    print("Números listados: ", Num_listados)
    for numero in Num_listados:
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
