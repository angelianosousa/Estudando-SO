from base_project import pop_vector_thread, show_counter_thread

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
  v_counter        = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

  thread_pop       = pop_vector_thread(1, 'pop_vetor', v_random_numbers)
  thread_count     = show_counter_thread(2, 'Counter_x_to_y', v_random_numbers, v_counter)
  thread_pop.start()
  thread_count.start()

  # Com vetor teste
  # thread_teste = myThread(1, 'thread_teste', v_teste, v_contagem, 1)
  # thread_teste.start()

main()