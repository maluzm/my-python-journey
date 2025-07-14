'''
CONSTANTE = variaveis que não vão mudar
muitas condições(if, else) são ruins para codigos
muita complexidade é ruim
'''
"""
velocidade = 60
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 100
RANGE_RADAR = 1

if velocidade > RADAR_1:
    print('Acma do limite de velocidade')

if local_carro >= (LOCAL_1 - RANGE_RADAR) and local_carro <= (LOCAL_1 + RANGE_RADAR) and velocidade > RADAR_1:
    print('Dentro do Range do Radar')
"""

velocidade = 60
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 100
RANGE_RADAR = 1

#ação de tornar codigo mais legivel ao explicar o codigo
vel_do_carro_no_radar = velocidade > RADAR_1
carro_passou_no_radar = local_carro >= (LOCAL_1 - RANGE_RADAR) and local_carro <= (LOCAL_1 + RANGE_RADAR)

if vel_do_carro_no_radar:
    print('Acma do limite de velocidade')

if carro_passou_no_radar and vel_do_carro_no_radar:
    print('Dentro do Range do Radar')