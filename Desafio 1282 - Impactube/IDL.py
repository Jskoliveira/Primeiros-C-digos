qt_canais=int(input())
lista_d_canais=[]
canal=[]
for i in range(0,qt_canais):
    
    nome,inscritos,monetizacao,premium=input().split(';')
    lista_d_canais.append([nome,inscritos,monetizacao,premium[:]])
    canal.clear()
    
x=float(input())
y=float(input())
    
print('-----')
print('BÔNUS')
print('-----')      
    
for ii in lista_d_canais:
    
    if ii[3]!='sim':
        ii[1]=int(ii[1])
        ii[2]=float(ii[2])
        if ii[1]//1000:
            resultado = (ii[1]//1000)* y + ii[2]
        else:
            resultado = ii[2]
        print(f'{ii[0]}: R$ {resultado:.2f}') 
        

    if ii[3]!='não':
        ii[1]=int(ii[1])
        ii[2]=float(ii[2])
        if ii[1]//1000:
            resultado = (ii[1]//1000)* x + ii[2]
        else:
            resultado = ii[2]
        print(f'{ii[0]}: R$ {resultado:.2f}') 
