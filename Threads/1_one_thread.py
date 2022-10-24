from base_project import print_vector_count, pop_vector_without_threads, counter_thread
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
    print('Start pop vector')
    pop_vector_without_threads(v_random_numbers)
    print('Finish pop vector')

    thread_count = counter_thread(1, 'Counter_0_to_9', v_random_numbers, dic_contagem, 0, 9)

    start_time = time.time()
    thread_count.start()
    thread_count.join()
    
    # To start filling the vector and counting
    end_time = time.time()

    timer_run = end_time - start_time
    time_total += timer_run
    v_random_numbers = []

    print(f'Time of execution timer {i}: {timer_run}')
    print(f'Total of execution right now: {time_total}')

  print_vector_count(dic_contagem)
  print(f'Media time of execution: {time_total/RUNNER} seconds')

main()
