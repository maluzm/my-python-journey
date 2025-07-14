"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# MINHA SOLUÇÃO
numero = input('Digite um numero inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
        
    modulo_numero = numero_int % 2

    if modulo_numero == 0:
        print(f"O numero: {numero_int} é par")
    else: 
        print(f'O numero: {numero_int} é impar')
else:
    print(f'O valor informado: {numero} não é um inteiro')

#sOLUÇÃO SUGERIDAS
numero = input('Digite um numero inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    impar_par = numero_int % 2 == 0
    par_impar_txt = 'impar'

    if impar_par:
        par_impar_txt = 'par'

        print(f'O numero: {numero_int} é {par_impar_txt}')
else:
    print(f'O valor informado: {numero} não é um inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
'''hora = input('Que horas são? ')
hora_int = int(hora)

if hora_int <= 11:
    print(f"Bom dia")
elif hora_int > 11 and hora_int <= 17:
    print('Boa tarde')
else:
    print('Boa noite')'''


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Insira seu primeiro nome: ')
qntd_letras = len(nome)

if qntd_letras <= 4:
    print('seu nome é curto')
elif qntd_letras > 4 and qntd_letras <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')