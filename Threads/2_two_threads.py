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

    # thread_pop   = pop_vector_thread(1, 'pop_vetor', v_random_numbers)
    thread_count  = counter_thread(1, 'Counter_0_to_4', v_random_numbers, dic_contagem, 0, 4)
    thread_count1 = counter_thread(2, 'Counter_5_to_9', v_random_numbers, dic_contagem, 5, 9)

    threads.append(thread_count)
    threads.append(thread_count1)
      
    start_time = time.time()
    for t in threads:
      t.start()

    for t in threads:
      t.join()
    end_time = time.time()

    threads = []
    v_random_numbers = []

    timer_run   = end_time - start_time
    time_total += timer_run

    print(f'Time of execution timer {i}: {timer_run}')
    print(f'Total of execution right now: {time_total}')

  print_vector_count(dic_contagem)
  print(f'Media time of execution: {time_total/RUNNER} seconds')

main()
