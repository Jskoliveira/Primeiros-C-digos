p = 1
divida = int(input())
parcelas = int(input())

while divida >0:
      if divida <parcelas:
         antes=divida
         divida=divida-divida
         print('pagamento:',p)
         print('antes =',antes)
         print('depois =',divida)
         print('-----')
      else:
           antes = divida
           divida = divida - parcelas
           print('pagamento:',p)
           print('antes =',antes)
           print('depois =',divida)
           print('-----')
           p += 1
