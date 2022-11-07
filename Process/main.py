from multiprocessing import Array, Process, active_children
from time import time
import my_process

RUNNER = 30
total_time = 0
v_random_numbers = []
array_counter = Array('i', 10)

# This function is responsible for start ours process and showing up our array counter
def start_count(jobs, n_counting, last_media_time):
  if __name__ == '__main__':
    global v_random_numbers, total_time

    start_time = time()
    for job in range(len(jobs)):
      jobs[job].start()

    # At this point we are showing your array counter while this vector are incremented by position
    while len(active_children()) > 0:
      my_process.print_array_counter(array_counter, n_counting, last_media_time)

    for job in range(len(jobs)):
      jobs[job].join()
    end_time = time()

    time_of_execution = end_time - start_time
    total_time += time_of_execution
    v_random_numbers = []
  
  print(f'Time of execution {time_of_execution} seconds')
  print('=-='*13)

# Instance process are our 'constructor' for our processors selected on main function
def instance_process(n_process, jobs, semaphore):

  if n_process == 1:
    my_process.populate_vector(v_random_numbers)

    process = Process(name='Counter 0 to 9', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, 0, 9, semaphore))
    jobs.append(process)

  elif n_process == 2:
    my_process.populate_vector(v_random_numbers)

    for p in range(0, 10, 5):
      process = Process(name=f'Counter {p} to {p+4}', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, p, p+4, semaphore))
      jobs.append(process)

  elif n_process == 5:
    my_process.populate_vector(v_random_numbers)

    for p in range(0, 10, 2):
      process = Process(name=f'Counter {p} to {p+1}', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, p, p+1, semaphore))
      jobs.append(process)

  elif n_process == 10:
    my_process.populate_vector(v_random_numbers)

    for p in range(10):
      process = Process(name=f'Counter {p}', target=my_process.counter_numbers_on_array, args=(v_random_numbers, array_counter, p, p, semaphore))
      jobs.append(process)    

# And here are the all beginning and at the end we show the total of numbers are counting e media time of execution
def main():
  print('=-='*13)
  print('# Pick how much process do you want...')
  print('- 1 to 1 Process')
  print('- 2 to 2 Process')
  print('- 5 to 5 Process')
  print('- 10 to 10 Process')
  print('=-='*13)
  n_process = int(input())
  semaphore = input('Do you want semaphore too (y/n) ? ')
  jobs      = []
  print('=-='*13)

  for run in range(1, RUNNER+1):

    instance_process(n_process, jobs, semaphore)
    start_count(jobs, run, total_time)
    jobs = []
  
  print(f'Media time of execution: {total_time/RUNNER}')
  my_process.check_total_numbers_array(array_counter)

main()