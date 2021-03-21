# Leonardo Posso Benetti
# Python script que será executado em conjunto com o código em shell
# Este código é parte da resolução do processo seletivo de estágio da Cromai


# Importando as bibliotecas necessárias
import os
import time
import logging
import sys

# configura as opções de log
logging.basicConfig(filename="cromai.log", filemode='a', format='%(asctime)s-%(process)d-%(levelname)s-%(message)s')

# segundos entre as iterações de "i am alive"
x = 2


# extrai a ID do processo que está executando este código
try:
    pid = os.getpid()
except Exception as e:
    logging.error("Error in getting process ID", exc_info=True)
    sys.exit(1)


# abre o arquivo pid e escreve o ID do processo nele
try:
    file = open('pid', 'w')
except Exception as e:
    logging.error("Error in opening file", exc_info=True)
    sys.exit(1)

try:
    file.write(f"{pid}")
except Exception as e:
    logging.error("Error in writing to file", exc_info=True)
    sys.exit(1)

# fecha o arquivo
file.close()

# loop para imprimir "i am alive" 3 vezes
for i in range(3):
    print("2: I am alive")
    # para a execução por x segundos
    time.sleep(x)

# imprime a última mensagem
print("2: I gonna die now, bye")

