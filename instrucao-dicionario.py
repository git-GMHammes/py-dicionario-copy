#
# Dicionário var:{
#               subVar:valVar
#            }
#
clientes = {  # Tabela cliente no dicionário
    'id1': {
        'nome': 'Gustavo Hammes',
        'telefone': '(21)98055-8545',
    },
    'id3': {
        'nome': 'Luiz Melo',
        'telefone': '(21)96555-8577',
    },
    'id4': {
        'nome': 'Maria Creuza',
        'telefone': '(21)92345-8447',
    },
}
for chave_k, cliente_v in clientes.items():
    print(f'\n Exibindo {chave_k}')
    for dados_k, dados_v in cliente_v.items():
        print(f'\t {dados_k}: {dados_v}')
