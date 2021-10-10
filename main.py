users = []
while True:
    print('=' * 30)
    client = {'nome': str(input('Nome do Cliente: ')), 'idade': int(input('Idade do Cliente: '))}
    if client not in users:
        users.append(client)
        print('Cadastrado')
    else:
        print('Cliente ja Cadastrado')

    r = str(input('Quer Continuar S/N'))
    if r in 'Nn':
        break

print('='*30)
for u in users:
    print('Clientes Cadastrados:  {} - {} '.format(u['nome'], u['idade']))