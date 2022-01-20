dias = ['domingo','segunda','terca','quarta','quinta','sexta','sabado','domingo','segunda','terca','quarta','quinta','sexta','sabado']
compra=input()
prazo=int(input())

if prazo==0:
    print('chega hoje!')
else:             
 chegada=dias.index(compra)+prazo
 print(f'sera entregue',dias[chegada])
