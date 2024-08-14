name = input('Nome: ')

valid_grade = False 
while valid_grade == False:
    grades = input('Digite as notas separadas por espaço: ')
    try:
        GradeSplit = [float(grade) for grade in grades.split()]
        if any(grade < 0 or grade > 10 for grade in GradeSplit):
            print('nota inválida. Valor deve ser entre 0 e 10')
        else:
            valid_grade = True
    except ValueError:
        print('Nota Inválida. Use apenas números e separe os decimais com ponto. (EX. 9.5)')
        
valid_falta = False
while not valid_falta:
    try:
        faltas = int(input('Digite o total de faltas: '))
        if faltas < 0 or faltas > 20:
            print('Número de faltas inválido. Digite um valor de 0 a 20 aulas.')
        else:
            valid_falta = True
    except ValueError:
        print('Valor inválido. Use apenas números inteiros como 1, 2, 3...')

media = sum(GradeSplit) / len(GradeSplit)
falta = (20-faltas) / 20

if media > 6 and falta > 0.7:
    print(f'Aluno {name} Aprovado com a média de {media:.2f} e presença de {falta * 100:.1f}% Necessário 70%')
    
elif media > 6 and falta <= 0.7:
    print(f'Aluno Reprovado por falta: {falta * 100:.1f}% Necessário 70%')

elif media <= 6 and falta > 0.7:
    print(f'Aluno Reprovado por média baixa: {media:.2f}')

else:
    print(f'Aluno Reprovado Média: {media:.2f} Presença de {falta * 100:.1f}% Necessário 70%')
