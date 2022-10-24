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
    
    # Threads for counter the numbers
    thread_count0 = counter_thread(0, 'Counter_0', v_random_numbers, dic_contagem, 0, 0)
    thread_count1 = counter_thread(1, 'Counter_1', v_random_numbers, dic_contagem, 1, 1)
    thread_count2 = counter_thread(2, 'Counter_2', v_random_numbers, dic_contagem, 2, 2)
    thread_count3 = counter_thread(3, 'Counter_3', v_random_numbers, dic_contagem, 3, 3)
    thread_count4 = counter_thread(4, 'Counter_4', v_random_numbers, dic_contagem, 4, 4)

    thread_count5 = counter_thread(5, 'Counter_5', v_random_numbers, dic_contagem, 5, 5)
    thread_count6 = counter_thread(6, 'Counter_6', v_random_numbers, dic_contagem, 6, 6)
    thread_count7 = counter_thread(8, 'Counter_7', v_random_numbers, dic_contagem, 7, 7)
    thread_count8 = counter_thread(8, 'Counter_8', v_random_numbers, dic_contagem, 8, 8)
    thread_count9 = counter_thread(9, 'Counter_9', v_random_numbers, dic_contagem, 9, 9)

    threads.append(thread_count0)
    threads.append(thread_count1)
    threads.append(thread_count2)
    threads.append(thread_count3)
    threads.append(thread_count4)

    threads.append(thread_count5)
    threads.append(thread_count6)
    threads.append(thread_count7)
    threads.append(thread_count8)
    threads.append(thread_count9)

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

    print(f'Time of execution timer {i}: {timer_run}')
    print(f'Total of execution right now: {time_total}')

  print_vector_count(dic_contagem)
  print(f'Media time of execution: {time_total/RUNNER} seconds')

main()