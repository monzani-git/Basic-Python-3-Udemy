import time 
import matplotlib.pyplot as plt


palavras = []
tempos = []
for i in range(5):
    inicio_tempo = time.time()
    palavra = input('Digite 5 palavras, (ao finalizar uma, confirme com Enter): ')
    fim_tempo = time.time()
    tempo = fim_tempo - inicio_tempo
    palavras.append(palavra)
    tempos.append(tempo)
    
print(tempos)

plt.plot(palavras, tempos, marker='o')
plt.xlabel('Palavras')
plt.ylabel('Tempo (segundos)')
plt.title('Tempo para digitar cada palavra')
plt.show()