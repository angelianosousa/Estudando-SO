from random import randint
from threading import Thread
import time

exitFlag = 0
VECTOR_LENGHT = 10**4

# class populate our principal vector
class pop_vector_thread(Thread):
  def __init__(self, ThreadID, name, v_random_numbers):
    Thread.__init__(self)
    self.ThreadID             = ThreadID
    self.name                 = name
    self.v_random_numbers     = v_random_numbers
  def run(self):
    pop_vector(self.v_random_numbers, self.name, 1)

# class count numbers in our principal vector async
class counter_thread(Thread):
  def __init__(self, ThreadID, name, v_random_numbers, v_counter, start_with, end_with):
    Thread.__init__(self)
    self.ThreadID             = ThreadID
    self.name                 = name
    self.v_random_numbers     = v_random_numbers
    self.v_counter            = v_counter
    self.start_with           = start_with
    self.end_with             = end_with
  def run(self):
    count_numbers(self.v_random_numbers, self.v_counter, self.start_with, self.end_with)

# Funcion that populate our principal vector
def pop_vector(vector, threadName, show_count):
  while show_count:
    if exitFlag:
      threadName.exit()
    for i in range(VECTOR_LENGHT):
      vector.insert(i, randint(0, 9))
    show_count -= 1

# Função que mostra o vetor contagem para acompanhar os números
def print_vector_count(dic_contagem):
  # show_count = 1
  # while show_count:
  #   if exitFlag:
  #     threadName.exit()
    # sleep(1) # This line is responsable for showing the v_counter in a way confortable for the user
    print('-=-'*10)
    print('  # -=====- Teste -=====- #')
    print('-=-'*10)

    for key, value in dic_contagem.items():
      print(f'| {key} <-> {value}')
    # show_count -= 1

# Função para realizar a contagem e armazenar no vetor conforme a posição
def count_numbers(vetor, dic_contagem, start_with, end_with):
  number_increment = 0

  for i in range(VECTOR_LENGHT):
    for start_with in range(end_with+1):
      if vetor[i] == start_with:
        dic_contagem[str(start_with)] += 1
        number_increment = start_with

    print_vector_count(dic_contagem)
    print('='*30)
    print(f'Length: {len(vetor)}')
    print(f'Number increment: {number_increment}')

def sum_numbers_count(dic_contagem):
  sum = 0
  for k, v in dic_contagem.items():
    sum += v
  
  print(f'Dic Contagem: {sum}')