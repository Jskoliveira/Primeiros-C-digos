Valor=float(input())
Quant=int(input())
Desc=0.10+(Quant*1)/100
Total1=(Valor*Quant)
Total2=(Valor*Quant)-(Valor*Quant*Desc)
print(f'%.2f' % Total1)
print(f'%.2f' % Total2)
