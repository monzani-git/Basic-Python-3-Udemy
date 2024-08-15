import requests
import json
import Functions

coordenadas = Functions.get_coordinates()
local = Functions.get_local_code(coordenadas['lat'], coordenadas['long'])
ClimaAtual = Functions.get_present_condition(local['codigo_local'], local['nome_local'])

print("Clima atual em: " + (ClimaAtual['nome_local']))
print("Temperatura: ", ClimaAtual['temperatura'])