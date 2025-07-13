'''
Exercicio
Peça ao usuatrio para digitar seu nome
PEça ao usuario para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome E [nome]
        Seu nome invertido é [nome invertido]
        Seu nome contém (ou não) espaços
        Seu nome tem [n] letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade exiba:
'Desculpe voce deixou campos vazios
'''

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

tamanho = len(nome)

if nome == '' or idade == '': 
    print('Desculpe você deixou espaços em branco')
else:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')
    print(f'Seu nome tem {tamanho} letras')
    print(f'A primeira letra do seu nome é: {nome[:1]}')
    print(f'A ultima letra do seu nome é: {nome[-1:]}')

# Resolução professor
if nome and idade: 
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')

    print(f'Seu nome tem {tamanho} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')

else:
    print('Desculpe você deixou espaços em branco')