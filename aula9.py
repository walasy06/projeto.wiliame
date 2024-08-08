a = int(input("Informe o primeiro número inteiro (a): "))
b = int(input("Informe o segundo número inteiro (b): "))
if a < b:
    soma = 0
    for i in range(a, b + 1):
        soma += i
    print(f"A soma dos números inteiros no intervalo [{a}, {b}] é: {soma}")
else:
    print("Erro: O primeiro número (a) deve ser menor que o segundo número (b).")

primeiro_termo = int(input("Informe o primeiro termo da PA: "))
quantidade_termos = int(input("Informe a quantidade de termos da PA: "))
razao = int(input("Informe a razão da PA: "))
for i in range(1, quantidade_termos + 1):
    termo = primeiro_termo + (i - 1) * razao
    print(f"Termo {i}: {termo}")
