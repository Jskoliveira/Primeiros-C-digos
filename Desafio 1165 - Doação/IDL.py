doacao=0
while True:
      vc=float(input())
      doacao += vc
      if vc<0:
        doacao-=vc
        print(f'VC$ {doacao:.2f}')
        print(f'R$ {doacao*2.5:.2f}')
        break
