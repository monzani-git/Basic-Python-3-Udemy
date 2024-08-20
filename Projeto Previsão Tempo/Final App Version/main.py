import requests
import json
import datetime
import Functions

try:
    coordenadas = Functions.get_coordinates()
    local = Functions.get_local_code(coordenadas['lat'], coordenadas['long'])
    ClimaAtual = Functions.get_present_condition(local['codigo_local'], local['nome_local'])
    
    print("Clima atual em: " + (ClimaAtual['nome_local']))
    print(f"Temperatura: {ClimaAtual['temperatura']} \xb0C - {ClimaAtual['text_clima']}")
    print('\nClima para hoje e para os proximos dias: \n',)
    
    semana = Functions.get_daily(local['codigo_local'])
    
    for dia in semana:
        
        traducao_dias_semana = {
        'Monday': 'Segunda-feira',
        'Tuesday': 'Terça-feira',
        'Wednesday': 'Quarta-feira',
        'Thursday': 'Quinta-feira',
        'Friday': 'Sexta-feira',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }
        
        data = datetime.datetime.fromtimestamp(dia['dia'])
        dia_da_semana_ingles = data.strftime('%A')
        dia_da_semana = traducao_dias_semana[dia_da_semana_ingles]
        
        print(dia_da_semana)
        print(f"Minima: {(dia['min'] - 32) * 5 / 9:.1f}°C")
        print(f"Máxima: {(dia['max'] - 32) * 5 / 9:.1f}°C")
        print(f"Clima: {dia['clima']}")
        print("------------------")

except:
    print('Erro ao Processar Solicitação. Entre em contato com Administrador')