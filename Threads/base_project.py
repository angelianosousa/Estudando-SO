from random import randint
import threading
import time

exitFlag = 0
VECTOR_LENGHT = 10**8
threadLock = threading.Lock()

# class populate our principal vector
class pop_vector_thread(threading.Thread):
  def __init__(self, ThreadID, name, v_random_numbers):
    threading.Thread.__init__(self)
    self.ThreadID             = ThreadID
    self.name                 = name
    self.v_random_numbers     = v_random_numbers
  def run(self):
    pop_vector(self.v_random_numbers, self.name)

# class count numbers in our principal vector async
class counter_thread(threading.Thread):
  def __init__(self, ThreadID, name, v_random_numbers, v_counter, start_with, end_with):
    threading.Thread.__init__(self)
    self.ThreadID             = ThreadID
    self.name                 = name
    self.v_random_numbers     = v_random_numbers
    self.v_counter            = v_counter
    self.start_with           = start_with
    self.end_with             = end_with
  def run(self):
    count_numbers(self.v_random_numbers, self.v_counter, self.start_with, self.end_with, self.name)

# Funcion that populate our principal vector
def pop_vector(vector, threadName):
  show_count = 1

  while show_count:
    if exitFlag:
      threadName.exit()
    for i in range(VECTOR_LENGHT):
      vector.insert(i, randint(0, 9))
    show_count -= 1

# Função que mostra o vetor contagem para acompanhar os números
def print_vector_count(dic_contagem):
  print('=-='*12)
  print(f'  # -=====- Show counter -=====- #')
  print('=-='*12)

  for key, value in dic_contagem.items():
    print(f'| {key} <-> {value}')

# Função para realizar a contagem e armazenar no vetor conforme a posição
def count_numbers(vetor, dic_contagem, start_with, end_with, threadCount = ''):
  number_increment = 0

  if threadCount == '':
    for i in range(VECTOR_LENGHT):
      for j in range(start_with, end_with+1):
        if vetor[i] == j:
          dic_contagem[str(j)] += 1
          number_increment = j

      print_vector_count(dic_contagem)
      print('='*30)
      print(f'Length: {len(vetor)}')
      print(f'Number increment: {number_increment}')
  else:
    show_count = 1

    while show_count:
      if exitFlag:
        threadCount.exit()

      for i in range(VECTOR_LENGHT):
        for j in range(start_with, end_with+1):
          if vetor[i] == j:
            dic_contagem[str(j)] += 1
            number_increment = j
        threadLock.acquire()
        print_vector_count(dic_contagem)
        threadLock.release()
        print('='*30)
        print(f'Length: {len(vetor)}')
        print(f'Number increment: {number_increment}')
      show_count -= 1

def sum_numbers_count(dic_contagem):
  sum = 0
  for k, v in dic_contagem.items():
    sum += v
  
  print(f'Dic Contagem: {sum}')