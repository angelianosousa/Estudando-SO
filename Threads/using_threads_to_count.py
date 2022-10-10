from random import randint
import threading
import time

exitFlag = 0

# Função para criar e popular o vetor principal
def popular_vetor(vetor):
  for i in range(1000):
    vetor.append(randint(0, 9))

# Função para realizar a contagem e armazenar no vetor conforme a posição
def count_numbers(vetor, v_count):
  for i in range(len(vetor)):
    if vetor[i] == 0:
      v_count[0] += 1
    elif vetor[i] == 1:
      v_count[1] += 1
    elif vetor[i] == 2:
      v_count[2] += 1
    elif vetor[i] == 3:
      v_count[3] += 1
    elif vetor[i] == 4:
      v_count[4] += 1
    elif vetor[i] == 5:
      v_count[5] += 1
    elif vetor[i] == 6:
      v_count[6] += 1
    elif vetor[i] == 7:
      v_count[7] += 1
    elif vetor[i] == 8:
      v_count[8] += 1
    elif vetor[i] == 9:
      v_count[9] += 1

    print_vector_count(v_count, 'thread_teste', 1, 1)

class myThread(threading.Thread):
  def __init__(self, ThreadID, name, v_random_numbers, v_count, delay):
    threading.Thread.__init__(self)
    self.ThreadID             = ThreadID
    self.name                 = name
    self.v_random_numbers     = v_random_numbers
    self.v_count              = v_count
    self.delay                = delay
  def run(self):
    print(f'Starting Count: {self.name}')
    count_numbers(self.v_random_numbers, self.v_count)

# Função que mostra o vetor contagem para acompanhar os números
def print_vector_count(vetor, threadName, delay, show_count):
  while show_count:
    if exitFlag:
      threadName.exit()
    time.sleep(delay)
    print(f'-===== {threadName} =====-')
    for i in range(len(vetor)):
      print(f'Contei: {i} -> {vetor[i]}')
    show_count -= 1

# Função principal
def main():
  # 100.000.000
  #  10.000.000
  #   1.000.000
  #     100.000
  v_teste = [
    1, 1, 1, 1,
    2, 2, 2, 2,
    3, 3, 3, 3
  ]
  # v_numeros_aleatorios = []
  v_contagem   = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  # popular_vetor(v_numeros_aleatorios)
  # thread01 = myThread(1, 'show_v_counter', v_numeros_aleatorios, v_contagem, 1)
  # thread01.start()

  # Com vetor teste
  thread_teste = myThread(1, 'thread_teste', v_teste, v_contagem, 1)
  thread_teste.start()

main()