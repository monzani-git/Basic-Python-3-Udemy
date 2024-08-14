fatura = 0
rep= input('Deseja adicionar outro produto? (s/n)')

while rep == 's':
    vendas = {
        'Nome do Produto': input('Nome do produto: '),
        'Preço do Produto': input('Preço do produto R$ ').replace(',', '.')
}

    preco = float(vendas['Preço do Produto'])
    vendas['Preço do Produto'] = preco

    fatura += vendas['Preço do Produto']
    rep= input('Deseja adicionar outro produto? (s/n)')

print(f'Sua fatura R$ {fatura:.2f}')
