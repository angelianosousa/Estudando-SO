from base_project import sum_numbers_count, pop_vector_thread, counter_thread, print_vector_count
import time
import threading

# Função principal
def main():
  v_random_numbers = []
  dic_contagem = { 
    '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, 
    '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
  }

  threads = []

  thread_pop    = pop_vector_thread(1, 'pop_vetor', v_random_numbers)
  # thread_count1 = counter_thread(2, 'Counter_0_to_2', v_random_numbers, dic_contagem, 0, 4)
  # thread_count2 = counter_thread(3, 'Counter_3_to_5', v_random_numbers, dic_contagem, 5, 9)

  thread_count1 = counter_thread(2, 'Counter_0_to_2', v_random_numbers, dic_contagem, 0, 0)
  # thread_count2 = counter_thread(3, 'Counter_3_to_5', v_random_numbers, dic_contagem, 3, 5)
  # thread_count3 = counter_thread(4, 'Counter_6_to_7', v_random_numbers, dic_contagem, 6, 7)
  # thread_count4 = counter_thread(5, 'Counter_8_to_9', v_random_numbers, dic_contagem, 8, 9)

  threads.append(thread_pop)
  threads.append(thread_count1)
  # threads.append(thread_count2)
  # threads.append(thread_count3)
  # threads.append(thread_count4)

  start_time = time.time()
  for t in threads:
   t.start()

  for t in threads:
   t.join()

  end_time = time.time()

  sum_numbers_count(dic_contagem)
  print(f'Time of execution: {end_time - start_time} seconds')

main()