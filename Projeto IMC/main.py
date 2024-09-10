import Functions

print('-----Vamos Calcular seu IMC-----')
print('--------------------------------')
print('\n')

valid_sex = False
while valid_sex == False:
    sexo = input('Sexo M ou F: ').lower()
    if sexo != 'm' and sexo != 'f':
        print('Sexo inválido. Digite M ou F')
    else:
        valid_sex = True
        print('\n')

valid_peso = False
while valid_peso == False:
    try:
        peso = float(input('Qual peso atual em Kg: '))
        if peso <= 0 or peso > 500:
            print('Peso iválido. Peso de 0 a 500 separado por ponto (Ex. 63.5)')
        else:
            valid_peso = True
        print('\n')
    except ValueError:
        print('Peso inválido. Use apenas numeros e separe o decimais com ponto.')

valid_altura = False       
while valid_altura == False:
    try:
        altura = float(input('Qual altura: '))
        if altura <= 0 or altura > 3:
            print('Altura Inválida. Altura deve ser de 0 a 3')
        else:
            valid_altura = True
            print('\n')
    except ValueError:
        print('Formato de altura inválido. Use ponto para separar os decimais (Ex. 1.72).')

imc_valor = Functions.imc(peso, altura)
classificacao = Functions.class_imc(sexo, imc_valor)

print('-----Resultado do seu IMC-----')
print('--------------------------------')
print('\n')
print(f'Seu IMC é de: {imc_valor:.2f}')
print(f'Sua classificação: {classificacao}')
print('\n')