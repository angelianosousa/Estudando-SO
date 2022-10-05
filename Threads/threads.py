from random import randint

# Função para criar e popular o vetor principal
def gerar_vetor(vetor):
  for vetor in range(10**8):
    vetor.append(randint(0, 10))

# Função para realizar a contagem e armazenar no vetor conforme a posição
def contar(vetor, v_contar):
  for i in range(len(vetor)):
    if vetor[i] == 1:
      v_contar[0] += 1

# Função que mostra o vetor contagem para acompanhar os números
def mostrar_contagem(vetor):
  for i in range(len(vetor)):
    print(f'{i}: {vetor[i]}')


def main():
  vetor_referencia = []
  vetor_contagem   = [0,]
  gerar_vetor(vetor_referencia)
  mostrar_contagem(vetor_contagem)
  # threads = int(input('Selecione o número de threads: '))

  # print(f"Threads escolhidas: {threads}")

  # aleatorio = randint(0, 9)
  # print(f'aleatorio: {aleatorio}')
  # contagem = [12, 5, 6, 7, 8, 9, 10, 5, 20, 30]

main()