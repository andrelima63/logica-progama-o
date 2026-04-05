nome = input("Digite seu nome"" ")
num1 = float(input("Digite o primeiro numero"))
num2 = float(input("Digite o segundo numero"))

print("Escolha a operação"" ")
print("1 - adição")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")
print("5 - porcentagem")

op = input("digite o numero da desejado para a resolução da questão"" ")

if op == "1":
  result = num1 + num2
  print(f"O resultado da adição é: {result}")
elif op == "2":
  result = num1 - num2
  print(f"O resultado da subtração é: {result}")
elif op == "3":
  result = num1 * num2
  print(f"O resultado da multiplicação é: {result}")
elif op == "4":
  result = num1 / num2
  print(f"O resultado da divisão é: {result}")
elif op == "5":
  result = num1 % num2
  print(f"O resultado da porcentagem é: {result}")

print("Muito Obrigado por participar", nome)
