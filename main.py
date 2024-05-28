
# Crie um dicionário em Python com os seguintes dados de uma pessoa:

# cria o dicionário
pessoa = {
    'Nome':'',
    'CPF':'',
    'RG':'',
    'Data de Nascimento':'',
    'Gênero':'', 
    'E-mail':'',
    'Telefone':'',
    'Tipo sanguíneo':'',
    'Profissão':'',
    'Empresa':'',
}

# Informar os dados da pessoa
pessoa ['Nome'] = input('Informe o Nome: ')
pessoa ['CPF'] = input('Informe o CPF: ')
pessoa ['RG'] = input('Informe o RG: ')
pessoa ['Data de Nascimento'] = input('Informe a Data de Nascimento: ')
pessoa ['Gênero'] = input('Informe o Gênero: ')
pessoa ['E-mail'] = input('Informe o E-Mail: ')
pessoa ['Telefone'] = input('Informe o Telefone: ')
pessoa ['Tipo sanguíneo'] = input('Informe o Tipo Sanguíneo: ')
pessoa ['Profissão'] = input('Informe a Profissão: ')
pessoa ['Empresa'] = input('Informe a Empresa: ')

# imprimir os dados inseridos
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')