inicio = int(input())-1
fim = int(input())
bissextos=0
while inicio<=fim-1:
      inicio+=1
      if inicio%4==0 and inicio%100!=0 or inicio%400==0:
          print(inicio)
          bissextos+=1
print('bissextos:',bissextos)
