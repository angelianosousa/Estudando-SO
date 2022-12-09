## Projeto 3 - Sistemas Operacionais Auditoria Linux

## Instale a ferramenta auditd na sua máquina

~~~
  sudo apt-get install auditd
~~~

<hr>

## Configurando arquivo para monitorar algo

### Passo 1
Criar um arquivo <b>something.rules</b> com suas regras de auditoria com o caminho /usr/share/audit/sample-rules/something.rules

### Passo 2
No terminal usar os comandos

~~~bash
  sudo service auditd start
~~~

### Passo 3
Acessar o arquivo de logs para acompanhar o processo com:

~~~bash
  tail -f /var/log/audit/audit.log
~~~

Consultar todos os eventos gerados pela nossa regra de auditoria

~~~
  ausearch -k nome_of_your_key
~~~

### Passo 4
Abra uma nova janela para carregar as regras do arquivo criado e escrito no passo 1 com o comando

~~~bash
  sudo auditctl -R /usr/share/audit/sample-rules/something.rules
~~~

### Passo 5
Você pode usar o comando 'cat' para acessar algum arquivo e então acompanhar o alerta na tela de logs

<br>

## Testes realizados

Vamos monitorar o acesso a nossa pasta de arquivos de estudo para as disciplinas do semestre adicionando as regras de auditoria no nosso arquivo <code>/usr/share/audit/sample-rules/something.rules</code> e então usar o comando abaixo para carregá-las

Antes de carregar o arquivo usemos <code>tail -f /var/log/audit/audit.log</code> para acompanharmos o monitoramento da pasta

Agora podemos carregar o arquivo e acessar a nossa pasta <b>Cadeiras</b>

~~~
  sudo auditctl -R /usr/share/audit/sample-rules/something.rules
~~~
