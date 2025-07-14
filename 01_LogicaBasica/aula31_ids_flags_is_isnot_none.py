"""
Id = identidade
Flag (bandeira) = marcar um local
is e is not = é ou não é (tipo, valor identidade)
none = não valor
"""

#ID = correponde a como o sistema vai procurar a varivael dentro da memoria, o nome daquela variavel dentro da memoria
v1 = "a"
print(id(v1)) # id:140704225640416

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Passou no if é True')
else:
    print('não passou no if, passou no if é false')

if passou_no_if is None: # is = é igual
    print(f'não passou no if, passou no if é: {passou_no_if}')

if passou_no_if is not None: # is not = não é igual
    print(f'passou no if, passou_no_if é: {passou_no_if}')