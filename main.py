usersName = list()
usersYear = list()

while True:
    print('=' * 30)

    n = str(input('Digite um Nome: '))
    if n not in usersName:
        usersName.append(n)
        print('Nome Cadastrado')
    i = int(input('Digite sua Idade: '))
    if i not in usersYear:
        usersYear.append(i)
        print('Idade Adicionada')
    else:
        print('Nome Duplicado')

    r = str(input('Quer Continuar S/N'))
    if r in 'Nn':
        break

print('='*30)
print('Nomes Cadastrados: {}'.format(usersName))
print('Idades Cadastradas: {}'.format(usersYear))
