A = int(input())
B = int(input())
if A>B:
    print('Nenhuma tabuada no intervalo!')
for tab in range(A,B+1):
    for num in range(1,11):
        resultado=tab * num 
        print(tab,'x',num,'=',resultado)
    print('-'*10)
