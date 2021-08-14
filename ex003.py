salarioHora = float(input('Quanto você ganha por hora? : '))
horaMes = int(input('Quantas horas trabalhadas por mês: ?'))

salario_bruto = salarioHora * horaMes
impostoRenda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

print ('* Salário Bruto : R$ %.2f' %salario_bruto)
print ('* Imposto Renda: R$ %.2f' %impostoRenda )
print ('* INSS: R$ %.2f' %inss )
print ('* Sindicato: R$ %.2f' %sindicato )
print ('* Salário Liquido : R$ %.2f' %(salario_bruto - impostoRenda - inss - sindicato))