from random import randint
from threading import Thread, Lock

exitFlag = 0
VECTOR_LENGHT = 10**8
threadLock = Lock()

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
    self.mutex                = 1
  def run(self):
    while self.mutex:
      if exitFlag:
        self.name.exit()
      for i in self.v_random_numbers:
        for j in range(self.start_with, self.end_with+1):
          if self.v_random_numbers[i] == j:
            increment_dictionary(self.dict_counter, j)
      self.mutex -= 1

# Function that fill our vector
def pop_vector_without_threads(vector):
  for i in range(VECTOR_LENGHT):
    vector.insert(i, randint(0, 9))

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
