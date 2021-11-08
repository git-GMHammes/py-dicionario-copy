#
# Dicionário Simples
# Utilizar dic1.update(dic2) Atualização de um dicionário com outro dicionário
#

dici1 = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd'
}
dici2 = {
    '001': 1001,
    '002': 1010,
    '003': 1020,
    '004': 1030
}
print(f'dici1: {dici1}')
dici1.update(dici2)
print(f'\n dici1.update(dici2): {dici1}')
