from multiprocessing import Array
from time import time
import my_process

RUNNER = 30
total_time = 0
v_random_numbers = []
array_counter = Array('i', 10)

if __name__ == '__main__':
  for i in range(RUNNER):
    my_process.populate_vector(v_random_numbers)
    print(f'Processing for the {i} time')

    process = my_process.Process(name='Counter 0 to 9', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 0, 9))
    # Counting the time of execution
    start_time = time()
    process.start()
    process.join()
    end_time = time()

    total_time += end_time - start_time
    v_random_numbers = []
    print(f'Time of execution: {end_time - start_time}')
    print('='*30)

print('='*15)
my_process.print_array_counter(array_counter)
my_process.check_total_numbers_array(array_counter)
print(f'Time of execution {total_time/RUNNER} seconds')
