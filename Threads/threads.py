from random import randint

# Função para criar e popular o vetor principal
def popular_vetor(vetor):
  for i in range(10000):
    vetor.append(randint(0, 9))

# Função para realizar a contagem e armazenar no vetor conforme a posição
def contar(vetor, v_contar):
  for i in range(len(vetor)):
    if vetor[i] == 0:
      v_contar[0] += 1
    elif vetor[i] == 1:
      v_contar[1] += 1
    elif vetor[i] == 2:
      v_contar[2] += 1
    elif vetor[i] == 3:
      v_contar[3] += 1
    elif vetor[i] == 4:
      v_contar[4] += 1
    elif vetor[i] == 5:
      v_contar[5] += 1
    elif vetor[i] == 6:
      v_contar[6] += 1
    elif vetor[i] == 7:
      v_contar[7] += 1
    elif vetor[i] == 8:
      v_contar[8] += 1
    elif vetor[i] == 9:
      v_contar[9] += 1

# Função que mostra o vetor contagem para acompanhar os números
def mostrar_contagem(vetor):
  for i in range(len(vetor)):
    print(f'Contei: {i} -> {vetor[i]}')

# Função principal
def main():
  v_referencia = []
  v_contagem   = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  popular_vetor(v_referencia)
  contar(v_referencia, v_contagem)
  mostrar_contagem(v_contagem)
  
  # print(f'Tamanho vetor referncia: {len(v_referencia)}')

main()