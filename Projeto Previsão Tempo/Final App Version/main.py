import requests
import json
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
        print(dia['dia'])
        print(f"Minima: {(dia['min'] - 32) * 5 / 9:.1f}°C")
        print(f"Máxima: {(dia['max'] - 32) * 5 / 9:.1f}°C")
        print(f"Clima: {dia['clima']}")
        print("----------------------")

except:
    print('Erro ao Processar Solicitação. Entre em contato com Administrador')