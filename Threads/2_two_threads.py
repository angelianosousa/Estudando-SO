from base_project import sum_of_positions, pop_vector_thread, counter_thread, print_vector_count
import time

def execute():
  time_total = 0

  v_random_numbers = []
  dic_contagem = { 
    '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, 
    '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
  }

  for i in range(0, 30):
    threads = []
    start_time   = time.time()

    thread_pop   = pop_vector_thread(1, 'pop_vetor', v_random_numbers)
    thread_count = counter_thread(2, 'Counter_1_to_1', v_random_numbers, dic_contagem, 0, 9)

    threads.append(thread_pop)
    threads.append(thread_count)
      
    for t in threads:
      t.start()

    for t in threads:
      t.join()

    threads = []
    v_random_numbers = []

    end_time = time.time()

    timer_run   = end_time - start_time
    time_total += timer_run
    print(f'Time of execution: {timer_run}')

  print_vector_count(dic_contagem)
  sum_of_positions(dic_contagem)
  print(f'Media time of execution: {time_total/30} seconds')

execute()
