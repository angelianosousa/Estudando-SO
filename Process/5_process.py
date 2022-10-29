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
    print(f'Processing for the {i} time')
    jobs = []
    my_process.populate_vector(v_random_numbers)

    process_0_to_1 = my_process.Process(name='Counter 0 to 1', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 0, 1))
    process_2_to_3 = my_process.Process(name='Counter 2 to 3', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 2, 3))
    process_4_to_5 = my_process.Process(name='Counter 4 to 5', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 4, 5))
    process_6_to_7 = my_process.Process(name='Counter 6 to 7', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 6, 7))
    process_8_to_9 = my_process.Process(name='Counter 8 to 9', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 8, 9))

    jobs.append(process_0_to_1)
    jobs.append(process_2_to_3)
    jobs.append(process_4_to_5)
    jobs.append(process_6_to_7)
    jobs.append(process_8_to_9)

    start_time = time()
    for process in jobs:
      process.start()
    
    for process in jobs:
      process.join()
    end_time = time()

    total_time += end_time - start_time
    v_random_numbers = []

print('='*15)
my_process.print_array_counter(array_counter)
my_process.check_total_numbers_array(array_counter)
print(f'Media time of execution {total_time/RUNNER} seconds')