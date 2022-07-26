calculadora

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = int(input('Informe qual operação você deseja realizar: \n, 1-soma \n, 2-subtração \n, 3-multiplicação \n, 4-divisão\n,   '))

def calculadora(num1, num2, operacao):
	if operacao == 1:
		resultado = num1 + num2
	elif operacao == 2:
		resultado = num1 - num2
	elif operacao == 3:
		resultado = num1 * num2
	elif operacao == 4:
		resultado = num1 / num2
	else:
		resultado = 0
	return resultado

resultado = str(calculadora(num1, num2, operacao))
print('O resultado é igual a ' + resultado)