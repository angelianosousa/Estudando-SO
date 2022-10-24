from base_project import pop_vector_without_threads, print_vector_count, counter_thread
import time

RUNNER = 30

def main():
  time_total = 0

  v_random_numbers = []
  dic_contagem = { 
    '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, 
    '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
  }

  for i in range(0, RUNNER):
    threads = []

    print('Start pop vector')
    pop_vector_without_threads(v_random_numbers)
    print('Finish pop vector')

    thread_count1 = counter_thread(1, 'Counter_0_to_1', v_random_numbers, dic_contagem, 0, 1)
    thread_count2 = counter_thread(2, 'Counter_2_to_3', v_random_numbers, dic_contagem, 2, 3)
    thread_count3 = counter_thread(3, 'Counter_4_to_5', v_random_numbers, dic_contagem, 4, 5)
    thread_count4 = counter_thread(4, 'Counter_6_to_7', v_random_numbers, dic_contagem, 6, 7)
    thread_count5 = counter_thread(5, 'Counter_8_to_9', v_random_numbers, dic_contagem, 8, 9)

    # threads.append(thread_pop)
    threads.append(thread_count1)
    threads.append(thread_count2)
    threads.append(thread_count3)
    threads.append(thread_count4)
    threads.append(thread_count5)

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

    print(f'Execution timer {i}: {timer_run} seconds')
    print(f'Total of execution right now: {time_total} seconds')

  print_vector_count(dic_contagem)
  print(f'Media time of execution: {time_total/RUNNER} seconds')

main()
