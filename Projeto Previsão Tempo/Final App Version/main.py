import requests
import json
import Functions

try:
    coordenadas = Functions.get_coordinates()
    local = Functions.get_local_code(coordenadas['lat'], coordenadas['long'])
    ClimaAtual = Functions.get_present_condition(local['codigo_local'], local['nome_local'])
    print("Clima atual em: " + (ClimaAtual['nome_local']))
    print(f"Temperatura: {ClimaAtual['temperatura']} \xb0C - {ClimaAtual['text_clima']}")
except:
    print('Erro ao Processar Solicitação. Entre em contato com Administrador')
