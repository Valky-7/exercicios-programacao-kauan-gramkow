# Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

# F - Feminino
# M - Masculino
# Sexo Inválido.
# Desenvolvido por Kauan Gramkow

letra = str(input("Qual é o seu sexo? (M/F) ")).upper()
if letra == "F":
    print("F - Feminino")
elif letra == "M":
    print("M - masculino")
else:
    print("Sexo Inválido.")