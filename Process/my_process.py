from multiprocessing import current_process, Semaphore
from random import randint
# from time import sleep

GENERATE_NUMBERS = 10**7

def populate_vector(vector):
  print('Start populate the vector...')
  for i in range(GENERATE_NUMBERS):
    vector.insert(i, randint(0, 9))

def check_total_numbers_array(array_counter):
  sum = 0
  for value in array_counter:
    sum += value

  print(f'Total numbers: {sum}')

def print_array_counter(array_counter):
  for i in range(0, 10):
    print(f'{i} <-> {array_counter[i]}')

def counter_numbers_on_array(v_random_numbers, array_counter, start_in, ends_in, semaphore):

  print(f'Start {current_process().name}...')
  if semaphore == 'y':
    semaphore = Semaphore(1) if semaphore == 'y' else Semaphore(0)
    with semaphore:
      for p in v_random_numbers:
        for key in range(start_in, ends_in+1):
          if v_random_numbers[p] == key:
              array_counter[key] += 1
  else:
    for p in v_random_numbers:
      for key in range(start_in, ends_in+1):
        if v_random_numbers[p] == key:
            array_counter[key] += 1
          