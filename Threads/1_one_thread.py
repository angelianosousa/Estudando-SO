from base_project import count_numbers, sum_numbers_count, pop_vector_thread
import time

def execute():
  v_random_numbers = []
  dic_contagem = { 
    '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, 
    '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
  }

  start_time = time.time()
  thread_pop = pop_vector_thread(1, 'pop_vetor', v_random_numbers)
  thread_pop.start()
  count_numbers(v_random_numbers, dic_contagem, 0, 9)
  end_time = time.time()

  sum_numbers_count(dic_contagem)
  print(f'Time of execution: {end_time - start_time} seconds')

execute()
