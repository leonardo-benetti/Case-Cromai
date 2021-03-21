## Case Cromai - Estágio de Desenvolvimento de Software Embarcado III 2021
## Leonardo Posso Benetti

 Este repositório se trata da minha solução de um case passado pela empresa Cromai como parte de seu processo seletivo.
 
 Os programas fornecidos foram desenvolvidos em uma máquina virtual Ubuntu 20.04.2 LTS.
 
 Esta entrega contém:
  - Um arquivo "pseudocodigo.txt" com um modelo preliminar conceitual de como seriam os programas desenvolvidos
  - Um arquivo "pythonscript.py" com o script python requisitado
  - Um arquivo "shellcode.sh" com o script shell requisitado
  - Um arquivo "resolucao_leonardo.pdf" com uma discussão de o que foi realizado para resolver o case

 Para correta execução dos programas fornecidos é necessário que os arquivos "pythonscript.py" e "shellcode.sh" estejam no mesmo diretório.
 Para executar o código shell basta executar a linha de comando:
   
   ./shellcode.sh
   
 O código shell executará o script python durante sua execução. 
 Para executar o programa em python separadamente pode-se executar a linha de comando:
 
   python3 pythonscript.py
   
 O programa python criará (ou atualizará, se já existente) o arquivo "pid" com seu ID de processo. Caso ocorra algum erro na criação ou escrita deste arquivo, o programa será suspenso e criará o arquivo "cromai.log" com informações do erro ocorrido.
