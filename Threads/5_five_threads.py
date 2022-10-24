from base_project import sum_of_positions, print_vector_count, pop_vector_thread, counter_thread
import time

# Função principal
def main():
  time_total = 0

  v_random_numbers = []
  dic_contagem = { 
    '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, 
    '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
  }

  for i in range(0, 30):
    threads = []
    thread_pop    = pop_vector_thread(1, 'pop_vetor', v_random_numbers)
    thread_count1 = counter_thread(2, 'Counter_0_to_3', v_random_numbers, dic_contagem, 0, 2)
    thread_count2 = counter_thread(3, 'Counter_4_to_6', v_random_numbers, dic_contagem, 3, 5)
    thread_count3 = counter_thread(4, 'Counter_7_to_9', v_random_numbers, dic_contagem, 6, 7)
    thread_count4 = counter_thread(5, 'Counter_8_to_9', v_random_numbers, dic_contagem, 8, 9)

    threads.append(thread_pop)
    threads.append(thread_count1)
    threads.append(thread_count2)
    threads.append(thread_count3)
    threads.append(thread_count4)

    start_time = time.time()

    # To start filling the vector and counting
    for t in threads:
      t.start()

    for t in threads:
      t.join()

    end_time = time.time()

    threads = []
    v_random_numbers = []

    timer_run = end_time - start_time
    time_total += timer_run

    print(f'Time of execution: {timer_run}')

  print_vector_count(dic_contagem)
  sum_of_positions(dic_contagem)
  print(f'Media time of execution: {time_total/30} seconds')

main()
