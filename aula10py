cheapest_medicine_name = ""
cheapest_medicine_price = float('inf')  # Initialize with a very large number
total_price = 0
for i in range(5):
    medicine_name = input(f"Digite o nome do medicamento {i+1}: ")
    medicine_price = float(input(f"Digite o preço do medicamento {i+1}: "))
    total_price += medicine_price
    if medicine_price < cheapest_medicine_price:
        cheapest_medicine_name = medicine_name
        cheapest_medicine_price = medicine_price
average_price = total_price / 5
print(f"O medicamento mais barato é {cheapest_medicine_name} e custa R${cheapest_medicine_price:.2f}")
print(f"A média dos preços dos medicamentos é R${average_price:.2f}")

senha_correta = 123456
tentativas = 3
while tentativas > 0:
  senha = int(input("Digite sua senha: "))
  if senha == senha_correta:
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}. Seja bem-vindo ao nosso banco!")
    break
  else:
    tentativas -= 1
    if tentativas == 2:
      print("Senha incorreta! Você ainda tem 2 tentativas.")
    elif tentativas == 1:
      print("Senha incorreta! Você ainda tem 1 tentativa.")
    else:
      print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
       
