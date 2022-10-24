from base_project import sum_of_positions, pop_vector_thread, counter_thread, print_vector_count
import time

def main():
  time_total = 0

  v_random_numbers = []
  dic_contagem = { 
    '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, 
    '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
  }

  for i in range(0, 30):
    threads = []

    # Thread that populate my vector
    thread_pop    = pop_vector_thread(0, 'pop_vetor', v_random_numbers)
    
    # Threads for counter the numbers
    thread_count0 = counter_thread(0, 'Counter_0', v_random_numbers, dic_contagem, 0, 0)
    thread_count1 = counter_thread(1, 'Counter_1', v_random_numbers, dic_contagem, 1, 1)
    thread_count2 = counter_thread(2, 'Counter_2', v_random_numbers, dic_contagem, 2, 2)
    thread_count3 = counter_thread(3, 'Counter_3', v_random_numbers, dic_contagem, 3, 3)
    thread_count4 = counter_thread(4, 'Counter_4', v_random_numbers, dic_contagem, 4, 4)

    thread_count5 = counter_thread(5, 'Counter_5', v_random_numbers, dic_contagem, 5, 5)
    thread_count6 = counter_thread(6, 'Counter_6', v_random_numbers, dic_contagem, 6, 6)
    thread_count7 = counter_thread(8, 'Counter_7', v_random_numbers, dic_contagem, 7, 7)
    thread_count8 = counter_thread(8, 'Counter_8', v_random_numbers, dic_contagem, 8, 9)

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

    start_time = time.time()   # Start counter the time

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
  print(f'Time of execution: {time_total/30} seconds')

main()