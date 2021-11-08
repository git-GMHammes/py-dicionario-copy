#
# Dicionário utilizando copy()
#
import copy
dici1 = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: ('e', 'f')
}
dici2 = dici1.copy()
dici3 = copy.deepcopy(dici1)
dici2[3] = 'batata'
print(f'\n {dici1} \n {dici2}')

dici3[5] = ('Valor', 'alterado')
print(f'\n {dici1} \n {dici3}')
