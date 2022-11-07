from multiprocessing import Semaphore
from random import randint
from time import sleep

GENERATE_NUMBERS = 10**7

# Populate our vector with random numbers
def populate_vector(vector):
  print('Start populate the vector...')
  for i in range(GENERATE_NUMBERS):
    vector.insert(i, randint(0, 9))

# For check if total numbers are counting correctly
def check_total_numbers_array(array_counter):
  sum = 0
  for value in array_counter:
    sum += value

  print(f'Total numbers: {sum}')

# For showing our array counter
def print_array_counter(array_counter, n_counting, total_time):

  print('Real time counter...')
  print(f'Count number: {n_counting}')
  print(f'Last media time: {total_time/n_counting}')

  for i in range(0, 10):
    print(f'{i} <-> {array_counter[i]}')

  print('=-='*13)
  sleep(1)

# Is for counting the numbers on our array with random numbers and save the counting on array counter
def counter_numbers_on_array(v_random_numbers, array_counter, start_in, ends_in, semaphore):
  
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
