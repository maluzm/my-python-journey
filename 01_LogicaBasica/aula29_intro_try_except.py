'''
introdução ao try/except
try = tentar xecutar o codigo
except = erros no codigo ao tentar executar
'''


# é possivel usar if e Else para ersolver o problema, mas o if else é a apenas uma checagem de codição e não de erros

"""
numero_str = input('Vou dobrar o numero: ')
#isdigit é uma função que checa se os caraceteres na string são digitos(booleano retorna True ou False)
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float*2}')
else:
    print('o valor informado não é um numero')

"""

numero_str = input('Vou dobrar o numero: ')

#executa o cod até o erro
try:

    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float*2}')
except: #quando o erro ocorre em try, automaticamente executa except
    print('o valor informado não é um numero')