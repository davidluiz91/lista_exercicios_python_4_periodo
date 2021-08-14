sexo = int(input('Qual seu sexo: (Digite 1 para  Masculino) ou (2 para Feminino): '))
h = float(input('Qual sua Altura:'))
peso = float(input('Qual seu Peso:'))

pesoIdeal = (72.7*h) - 58 if sexo == 1 else (62.1*h) - 44.7

if peso < pesoIdeal:
	print('Abaixo do peso ideal!')
elif peso == pesoIdeal:
	print('Dentro do peso ideal!')
else:
	print('Acima do peso ideal!')
print ('Peso: %.2f / Peso ideal: %.2f' %(peso, pesoIdeal))