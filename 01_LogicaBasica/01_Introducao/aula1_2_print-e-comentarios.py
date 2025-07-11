#Aula 1 - função print, uso de comentarios e doc string
# comentários
print('Hello, World!') # mostra coisas na tela
print(123)
# o python ignora essa linha
""" DocString (não é um cometario, o python não ignora essa linha de código, ele lê não faz nada, mas mantém na memória)"""
''' doc string
múltiplas linha
'''
#Aula 2 - Uso de print, argumentos, separador(,), uso de SEP (definindo separador) e END(definindo o final do print)
print(12,23,34, sep="-") # sep define o valor do separador (,) aqui ele se tornou (-)
print(12,23,34, sep="-", end='\r\n') #end define o final da linha, no caso de fabrica o final da linha já é \r\n (pular linha), mas é possivel definir outros finais
print(12,23,34, sep="-", end='#') #end define o final da linha, no caso de fabrica o final da linha já é \r\n (pular linha), mas é possivel definir outros finais
print(12,23,34, sep="-")