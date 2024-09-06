nome = input('Digite um nome: ')

if 'a' or 'A' in nome:
    nome_minusculo = nome.lower()
    quantidade = nome_minusculo.count('a')
    print(f'Seu nome possui a letra A {quantidade} vezes.')
else:
    print('Seu nome não possui letra A')