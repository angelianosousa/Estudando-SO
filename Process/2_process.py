from multiprocessing import Array
from time import time
import my_process

RUNNER = 30
execution_one_time = 0
total_time = 0
v_random_numbers = []
array_counter = Array('i', 10)

if __name__ == '__main__':

  for i in range(0, RUNNER):
    jobs = []
    my_process.populate_vector(v_random_numbers)

    print(f'Processing for the {i} time')
    process_0_to_4 = my_process.Process(name='Counter 0 to 4', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 0, 4))
    process_5_to_9 = my_process.Process(name='Counter 5 to 9', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 5, 9))
    jobs.append(process_0_to_4)
    jobs.append(process_5_to_9)

    start_time = time()
    for process in jobs:
      process.start()
    
    for process in jobs:
      process.join()
    end_time = time()

    total_time += end_time - start_time
    v_random_numbers = []
    print(f'Time of execution: {end_time - start_time}')
    print('='*30)

print('='*15)
my_process.print_array_counter(array_counter)
my_process.check_total_numbers_array(array_counter)
print(f'Media time of execution {total_time/RUNNER} seconds')
