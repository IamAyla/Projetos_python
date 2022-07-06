#definando a calculadora
def calculator (num_1, num_2, op):
  result = 0

  if op == '+':
    result = num_1 + num_2
  elif op == '-':
    result = num_1 - num_2
  elif op == '*':
    result = num_1 * num_2
  elif op == '/':
    result = num_1 / num_2
  print('O resultado de {} {} {} é {}'.format(num_1, op, num_2, result))
  
#Recebendo as informações do usuário
num_1 = float(input('Qual o primeiro número?'))
num_2 = float(input('Qual o segundo número?'))
op = str(input('Qual a operação? (+, -, *, /) '))

#Rodando o código já definido com os inputs 
calculator(num_1, num_2, op)
