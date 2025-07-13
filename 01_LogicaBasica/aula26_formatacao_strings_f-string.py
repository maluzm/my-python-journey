'''

formataçãop basica de strings com f- string
s - string
d- int
f - float

.<numero de digitos>f
x ou X - HExadecimal
(Caractere)(><)¨(quantidade)
> - Esquerda preencher caracteres para esqquerda
< - Direita preencher caracteres para direita
¨Centro

Sinal - ou +
Ex: 0>-100,.1f
Conversion flags - !r, !s, !a
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:0^10}')
print(f'{1000.1122342347567:,.1f}')
print(f'{1000.1122342347567:+,.1f}')
print(f'{1000.1122342347567:0>+10,.1f}')
print(f'{1000.1122342347567:0=+10,.1f}')
print(f'o hexadecimal de 1500 é {1500:08x}')

'''
ABC
       ABC
ABC       
   ABC    
000ABC0000
1,000.1
+1,000.1
00+1,000.1
+001,000.1
o hexadecimal de 1500 é 000005dc
'''