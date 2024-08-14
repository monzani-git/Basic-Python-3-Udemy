import tkinter as tk
import func_imc

def calcular_imc():
    try:
        # Obter valores das entradas
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        sexo = entry_sexo.get().lower()

        # Calcular IMC
        imc_valor = func_imc.imc(peso, altura)
        classificacao = func_imc.class_imc(sexo, imc_valor)
        
        # Atualizar o label de resultado com o IMC e a classificação
        label_resultado.config(text=f"Seu IMC é: {imc_valor:.2f}\nClassificação: {classificacao}")
    except ValueError:
        # Mensagem de erro se houver problemas na conversão dos valores
        label_resultado.config(text="Por favor, insira valores válidos.")

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de IMC")

# Configurar o layout da tela
root.geometry("300x400")
root.configure(bg='white')

# Título
titulo = tk.Label(root, text="Calculadora de IMC", font=("Arial", 16, "bold"), bg='white')
titulo.pack(pady=10)

subtitulo = tk.Label(root, text="Descubra se está no peso ideal", font=("Arial", 12), bg='white')
subtitulo.pack(pady=5)

# Sexo
tk.Label(root, text="Sexo M ou F", font=("Arial", 12), bg='white').pack(pady=5)
entry_sexo = tk.Entry(root, font=("Arial", 12), width=10, bg='lightgray')
entry_sexo.pack(pady=5)

# Peso
tk.Label(root, text="Peso", font=("Arial", 12), bg='white').pack(pady=5)
entry_peso = tk.Entry(root, font=("Arial", 12), width=10, bg='lightgray')
entry_peso.pack(pady=5)

# Altura
tk.Label(root, text="Altura", font=("Arial", 12), bg='white').pack(pady=5)
entry_altura = tk.Entry(root, font=("Arial", 12), width=10, bg='lightgray')
entry_altura.pack(pady=5)

# Resultado
label_resultado = tk.Label(root, text="", font=("Arial", 12), bg='white')
label_resultado.pack(pady=15)

# Botão para calcular
botao_calcular = tk.Button(root, text="Calcular", font=("Arial", 12), command=calcular_imc)
botao_calcular.pack(pady=10)

# Iniciar o loop principal
root.mainloop()


