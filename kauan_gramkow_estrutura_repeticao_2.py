# Faça um programa que leia 5 números e informe o maior número.
# Desenvolvido por Kauan Gramkow

numeros = []

for i in range(5):
    numero = int(input(f"Informe o {i+1}º número: "))
    numeros.append(numero)

maior = max(numeros)
print(f"O maior número é {maior}.")