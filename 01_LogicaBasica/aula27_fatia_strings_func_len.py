'''
Fatiamento de strings
 012345678
 Ola mundo
-987654321
os numeros representam os indices das letras
Fatiamento(partes da string) = [inicio:fim:passo(de passo em passo fatia os caracteres)] [::]
Obs.: a função len retorna a qtd de carateres da str
'''
variavel = 'Ola Mundo'
print(variavel[4:8]) #Mund
print(variavel[-1:]) #ultima letra
print(variavel[:1]) #primeira letra

#len: conta caracteres
print(len(variavel)) #9 strings
print(len(variavel[4:8])) #Mund = 4 strings

#passo
print(variavel[::2]) #OaMno = pula de 2 em 2 as strings
print(variavel[::-1]) 
print(variavel[-1:-10:-1]) #inverter a string
