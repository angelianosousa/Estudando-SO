from multiprocessing import Array, Process
from time import time
import my_process

RUNNER = 1
total_time = 0
v_random_numbers = []
array_counter = Array('i', 10)

def start_count(n_process, jobs):
  if __name__ == '__main__':
    global v_random_numbers, total_time;

    start_time = time()
    for job in range(n_process):
      jobs[job].start()

    for job in range(n_process):
      jobs[job].join()
    end_time = time()

    total_time += end_time - start_time
    v_random_numbers = []
  
  print('='*30)
  my_process.print_array_counter(array_counter)
  my_process.check_total_numbers_array(array_counter)
  print(f'Time of execution {total_time/RUNNER} seconds')

def instance_process(n_process, jobs):

  if n_process == 1:
    my_process.populate_vector(v_random_numbers)

    process = Process(name='Counter 0 to 9', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 0, 9))
    jobs.append(process)

  elif n_process == 2:
    my_process.populate_vector(v_random_numbers)

    for p in range(0, 10, 5):
      process = Process(name=f'Counter {p} to {p+4}', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, p, p+4))
      jobs.append(process)

  elif n_process == 5:
    my_process.populate_vector(v_random_numbers)

    for p in range(0, 10, 2):
      process = Process(name=f'Counter {p} to {p+1}', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, p, p+1))
      jobs.append(process)

  elif n_process == 10:
    my_process.populate_vector(v_random_numbers)

    for p in range(10):
      process = Process(name=f'Counter {p}', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, p, p))
      jobs.append(process)

def main():
  n_process   = int(input('How many process: '))
  jobs        = []
  # trava     = int(input('Usign lock ?\n'))
  # semaphore = int(input('Using semaphore ?\n'))

  instance_process(n_process, jobs)
  start_count(n_process, jobs)
  # v_random_numbers = []

main()