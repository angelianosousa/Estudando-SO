from random import randint
from threading import Thread, Lock
import time

exitFlag = 0
VECTOR_LENGHT = 10**8
threadLock = Lock()

# class populate our principal vector async
class pop_vector_thread(Thread):
  def __init__(self, ThreadID, name, v_random_numbers):
    Thread.__init__(self)
    self.ThreadID             = ThreadID
    self.name                 = name
    self.v_random_numbers     = v_random_numbers
  def run(self):
    print('Start pop vector')
    threadLock.acquire()
    pop_vector(self.v_random_numbers, self.name, 1)
    threadLock.release()
    print('Finish pop vector')

# class count numbers in our principal vector async
class counter_thread(Thread):
  def __init__(self, ThreadID, name, v_random_numbers, dict_counter, start_with, end_with):
    Thread.__init__(self)
    self.ThreadID             = ThreadID
    self.name                 = name
    self.v_random_numbers     = v_random_numbers
    self.dict_counter         = dict_counter
    self.start_with           = start_with
    self.end_with             = end_with
  def run(self):
    show_count = 1
    while show_count:
      if exitFlag:
        self.name.exit()
      for i in self.v_random_numbers:
        for j in range(self.start_with, self.end_with+1):
          if self.v_random_numbers[i] == j:
            increment_dictionary(self.dict_counter, j)
      show_count -= 1

# Function that fill our vector
def pop_vector(vector, threadName, show_count):
  while show_count:
    if exitFlag:
      threadName.exit()
    for i in range(VECTOR_LENGHT):
      vector.insert(i, randint(0, 9))
    show_count -= 1

# Function that show that dictionary counter
def print_vector_count(dic_contagem):
  print('=-='*11)
  print(' # -===- Show Dictionary -===- #')
  print('=-='*11)

  for key, value in dic_contagem.items():
    print(f'| {key} <-> {value}')

# Function to start the counter
def count_numbers_without_thread(vetor, dic_contagem, start_with, end_with):
  for i in range(VECTOR_LENGHT):
    for j in range(start_with, end_with+1):
      if vetor[i] == j:
        increment_dictionary(dic_contagem, j)

# This function increment the dictionary and has a semaphore
def increment_dictionary(dic_contagem, position):
  threadLock.acquire()
  dic_contagem[str(position)] += 1
  threadLock.release()

# This function exist to confirm that counter is correct
def sum_of_positions(dic_contagem):
  sum = 0
  for k, v in dic_contagem.items():
    sum += v
