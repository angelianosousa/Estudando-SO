from base_project import time, pop_vector_thread, counter_thread, sum_numbers_count

def execute():
  v_random_numbers = []
  dic_contagem = { 
    '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, 
    '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
  }
  start_time = time.time()
  thread_pop    = pop_vector_thread(1, 'pop_vetor', v_random_numbers)
  thread_count1 = counter_thread(2, 'Counter_1_to_1', v_random_numbers, dic_contagem, 0, 9)

  thread_pop.start()
  thread_count1.start()

  thread_pop.join()
  thread_count1.join()
  end_time = time.time()

  sum_numbers_count(dic_contagem)
  print(f'Time of execution: {end_time - start_time} seconds')

execute()