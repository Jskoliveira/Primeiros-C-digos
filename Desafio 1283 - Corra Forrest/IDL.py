tempos=[]
tempo=int(input())
tempos.append(tempo)

while (tempo > 0):
    tempo=int(input())
    tempos.append(tempo)
tempos.pop()
media=sum(tempos)/len(tempos)
print (f'MEDIA: {media:.2f}')

for tempo in tempos:
    if tempo < media:
        print(tempo)
