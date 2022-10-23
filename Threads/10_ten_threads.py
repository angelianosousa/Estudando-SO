from base_project import sum_numbers_count, pop_vector_thread, counter_thread, print_vector_count
import time

# Função principal
def main():
  v_random_numbers = []
  dic_contagem = { 
    '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, 
    '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
  }

  threads = []

  thread_pop    = pop_vector_thread(0, 'pop_vetor', v_random_numbers)
  
  thread_count0 = counter_thread(1, 'Counter_0', v_random_numbers, dic_contagem, 0, 0)
  thread_count1 = counter_thread(2, 'Counter_1', v_random_numbers, dic_contagem, 1, 1)
  thread_count2 = counter_thread(3, 'Counter_2', v_random_numbers, dic_contagem, 2, 2)
  thread_count3 = counter_thread(4, 'Counter_3', v_random_numbers, dic_contagem, 3, 3)

  thread_count4 = counter_thread(5, 'Counter_4', v_random_numbers, dic_contagem, 4, 4)
  thread_count5 = counter_thread(6, 'Counter_5', v_random_numbers, dic_contagem, 5, 5)
  thread_count6 = counter_thread(7, 'Counter_6', v_random_numbers, dic_contagem, 6, 6)
  thread_count7 = counter_thread(8, 'Counter_7', v_random_numbers, dic_contagem, 7, 7)
  thread_count8 = counter_thread(9, 'Counter_8_to_9', v_random_numbers, dic_contagem, 8, 9)

  threads.append(thread_pop)

  threads.append(thread_count0)
  threads.append(thread_count1)
  threads.append(thread_count2)
  threads.append(thread_count3)

  threads.append(thread_count4)
  threads.append(thread_count5)
  threads.append(thread_count6)
  threads.append(thread_count7)
  threads.append(thread_count8)

  start_time = time.time()
  for t in threads:
   t.start()

  for t in threads:
   t.join()

  end_time = time.time()

  sum_numbers_count(dic_contagem)
  print(f'Time of execution: {end_time - start_time} seconds')

main()