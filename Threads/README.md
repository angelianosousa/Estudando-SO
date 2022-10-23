# Projeto 01 - Trabalhando com Threads

## Descrição: Implementar um programa que faça as seguintes tarefas.
<hr>

* ✅ - Gerar um vetor de 10^8 posições preenchido aleatoriamento com algum dítigo entre 0 a 9.
* ✅ - Armazenar quantas vezes apareceu cada digito possível.
* ✅ - Exibir em tempo real a contagem de quantos digitos foram encontrados até o momento.
* ✅ - Permitir escolher quantas threads vão realizar a tarefa, variando entre 1, 2, 5 e 10.
* ✅ - Abordagem de como organizar as threads para realizar a busca é da equipe.
* ✅ - Garantir exclusão mútua usando as estratégias de semáforo e trava.
* ✅ - Repetir cada caso possível executar 30 vezes o experimento, ou seja, para os 10 casos existentes com a combinação número de threads e estratégia de exclusão mútua.
* ☑️ - Descrever no Documento a ser entregue a comparação da média de duração da execução em cada caso possível (número de threads e estratégia de exclusão mútua).

## Cenário para uso das threads
1. Somente 1 Thread
  - Usar a thread para exibir em tempo real a contagem do vetor, no primeiro momento sendo usada para popular o vetor e depois para exibir a contagem
2. Mais de 1 Thread
  - Usar 1 thread para exibir a contagem em tempo real
  - Usar as threads excedentes para popular o vetor, quando estiverem desocupadas...