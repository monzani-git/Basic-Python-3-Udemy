def imc (peso, altura):
    return peso / (altura ** 2)

valor_imc = imc

def class_imc (sexo, valor_imc):
    if sexo == 'm':
        if valor_imc < 20.7:
            return "Abaixo do peso"
        elif valor_imc >= 20.7 and valor_imc < 26.4:
            return "Peso Normal"
        elif valor_imc >= 26.4 and valor_imc < 27.8:
            return "Pouco Acima do Peso"
        elif valor_imc >= 27.8 and valor_imc< 31.1:
            return "Acima do peso ideal"
        elif valor_imc > 31.1:
            return "Obeso"

    elif sexo == 'f':
        if valor_imc < 19.1:
            return "Abaixo do peso"
        elif valor_imc >= 19.1 and valor_imc < 25.8:
            return "Peso Normal"
        elif valor_imc >= 25.8 and valor_imc < 27.3:
            return "Pouco Acima do Peso"
        elif valor_imc >= 27.3 and valor_imc < 32.3:
            return "Acima do peso ideal"
        elif valor_imc > 32.1:
            return "Obeso"
    else:
        return "Erro de cálculo. Netre em contato com administrador"