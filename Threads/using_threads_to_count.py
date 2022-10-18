from base_project import sum_numbers_count, count_numbers, pop_vector_thread, show_counter_thread, print_vector_count

# Função principal
def main():
  # 100.000.000
  #  10.000.000
  #   1.000.000
  #     100.000
  # v_teste = [
  #   1, 1, 1, 1,
  #   2, 2, 2, 2,
  #   3, 3, 3, 3
  # ]
  v_random_numbers = []
  dic_contagem = { 
    '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, 
    '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
  }

  threads_number = int(input('How many threads do you want ? (1 , 2, 5 or 10): '))

  if threads_number == 1:
    thread_pop     = pop_vector_thread(1, 'pop_vetor', v_random_numbers)
    thread_pop.start()
    count_numbers(v_random_numbers, dic_contagem)
  elif threads_number == 2:
    thread_pop     = pop_vector_thread(1, 'pop_vetor', v_random_numbers)
    thread_count1    = show_counter_thread(2, 'Counter_1_to_1', v_random_numbers, dic_contagem)

    thread_pop.start()
    thread_count1.start()

    thread_pop.join()
    thread_count1.join()
  else:
    print('Implementado...')

  sum_numbers_count(dic_contagem)
  
  # thread_count2     = show_counter_thread(3, 'Counter_2_to_2', v_random_numbers, v_counter)
  # thread_count3     = show_counter_thread(4, 'Counter_3_to_3', v_random_numbers, v_counter)
  # thread_count4     = show_counter_thread(5, 'Counter_4_to_4', v_random_numbers, v_counter)

  # thread_pop.join()
  # thread_count1.join()
  # thread_count2.start()
  # thread_count3.start()
  # thread_count4.start()

  # print('\n'*19)
  # print_vector_count(v_counter, 'Counter_1_to_1', 1)
  # print(f'Length: {len(v_random_numbers)}')

  # Com vetor teste
  # thread_teste = myThread(1, 'thread_teste', v_teste, v_contagem, 1)
  # thread_teste.start()

main()