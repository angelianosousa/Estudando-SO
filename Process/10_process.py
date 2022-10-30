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
    process_0 = my_process.Process(name='Counter 0', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 0, 0))
    process_1 = my_process.Process(name='Counter 1', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 1, 1))
    process_2 = my_process.Process(name='Counter 2', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 2, 2))
    process_3 = my_process.Process(name='Counter 3', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 3, 3))
    process_4 = my_process.Process(name='Counter 4', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 4, 4))

    process_5 = my_process.Process(name='Counter 5', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 5, 5))
    process_6 = my_process.Process(name='Counter 6', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 6, 6))
    process_7 = my_process.Process(name='Counter 7', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 7, 7))
    process_8 = my_process.Process(name='Counter 8', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 8, 8))
    process_9 = my_process.Process(name='Counter 9', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 9, 9))

    jobs.append(process_0)
    jobs.append(process_1)
    jobs.append(process_2)
    jobs.append(process_3)
    jobs.append(process_4)
    jobs.append(process_5)
    jobs.append(process_6)
    jobs.append(process_7)
    jobs.append(process_8)
    jobs.append(process_9)
    
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

my_process.print_array_counter(array_counter)
my_process.check_total_numbers_array(array_counter)
print(f'Media time of execution {total_time/RUNNER} seconds')
