#!/usr/bin/env python3
entrada_lista = input("Digite uma sequ�ncia de 04 n�meros: ")
Num_listados = list(map(int, entrada_lista.split()))
if len(Num_listados) != 4:
    print("Por favor, insira exatamente 04 n�meros!")
else:
    print("N�meros listados: ", Num_listados)
    for numero in Num_listados:
        if numero % 2 == 0:
            print(f"O n�mero {numero} � par.")
        else:
            print(f"O n�mero {numero} � �mpar.")
