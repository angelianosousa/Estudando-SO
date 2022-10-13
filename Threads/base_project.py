from random import randint
from threading import Thread
import time

exitFlag = 0
VECTOR_LENGHT = 10**8

class pop_vector_thread(Thread):
  def __init__(self, ThreadID, name, v_random_numbers):
    Thread.__init__(self)
    self.ThreadID             = ThreadID
    self.name                 = name
    self.v_random_numbers     = v_random_numbers
  def run(self):
    pop_vector(self.v_random_numbers, self.name, 1)

# Class responsable for creating a thread
class show_counter_thread(Thread):
  def __init__(self, ThreadID, name, v_random_numbers, v_counter):
    Thread.__init__(self)
    self.ThreadID             = ThreadID
    self.name                 = name
    self.v_random_numbers     = v_random_numbers
    self.v_counter            = v_counter
  def run(self):
    count_numbers(self.v_random_numbers, self.v_counter, self.name)

# Função para criar e popular o vetor principal
def pop_vector(vector, threadName, show_count):
  while show_count:
    if exitFlag:
      threadName.exit()
    for i in range(VECTOR_LENGHT):
      vector.insert(i, randint(0, 9))
    show_count -= 1

# Função que mostra o vetor contagem para acompanhar os números
def print_vector_count(vetor, threadName):
  show_count = 1
  while show_count:
    if exitFlag:
      threadName.exit()
    time.sleep(1) # This line is responsable for showing the v_counter in a way confortable for the user
    print(f'# -============================- #')
    print(f'# -=====- {threadName} -=====- #')
    print(f'# -============================- #')

    for i in range(len(vetor)):
      print(f'| {i} -> {vetor[i]}')
    show_count -= 1

# Função para realizar a contagem e armazenar no vetor conforme a posição
def count_numbers(vetor, v_count, threadName):
  number_increment = 0

  for i in range(len(vetor)):
    for j in range(9):
      if vetor[i] == j:
        v_count[j] += 1
        number_increment = j

    print('\n'*19)
    print_vector_count(v_count, threadName)
    print(f'Length: {len(vetor)}')
    print(f'Number increment: {number_increment}')