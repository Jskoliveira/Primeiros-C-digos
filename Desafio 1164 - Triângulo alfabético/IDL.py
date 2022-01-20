alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n=int(input())
n=n-1
m=0
while m<=n:
      posicao = alfabeto[0+m]+alfabeto[0+m]*m
      print(posicao)
      m+=1
