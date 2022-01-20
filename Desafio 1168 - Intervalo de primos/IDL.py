inicio=int(input())
fim=int(input())

def primo():
    
    contador=0
    
    for percorrer in range(1,inicio+1):
        if inicio%percorrer==0:
            contador+=1            
            
    if contador==2:
        print(inicio)
        return inicio
         
qtde_primo=0

while inicio < fim:
    inicio+=1
    chamar=primo()
    if chamar:
        qtde_primo+=1
        
print(f'primos:',qtde_primo)
