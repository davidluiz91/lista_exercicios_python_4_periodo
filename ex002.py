pesoPeixe = float(input("Qual é o peso do peixe? "))
if pesoPeixe > 50:
   print("Peixe acima do peso você pagará um multa de",(pesoPeixe - 50)*4 , "R$")
else:
   print("O peixe está em peso permitido.")