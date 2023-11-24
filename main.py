import tkinter as tk
from tkinter import ttk

# Definição das quantidades de ingredientes para cada fase
quantidades = {
    'pre_inicial': {'Milho': 63.00, 'Soja_Farelo_45%': 32.00, 'Nucleo_Inicial_Presence': 5.00},
    'inicial': {'Milho': 62.00, 'Soja_Farelo_45%': 30.00, 'Nucleo_Inicial_Presence': 5.00, 'Carne_e_Osso_45%_Farelo': 3.00},
    'crescimento': {'Milho': 78.00, 'Soja_Farelo_45%': 15.00, 'Nucleo_Inicial_Presence': 5.00, 'Calcario_calcitico': 2.00},
    'pre_postura': {'Milho': 65.80, 'Soja_Farelo_45%': 23.00, 'Nucleo_Postura_Total_4%': 4.00, 'Calcario_calcitico': 7.00, 'Sal': 0.200},
    'postura_ate_40_semanas': {'Milho': 62.50, 'Soja_Farelo_45%': 26.00, 'Nucleo_Postura_Total_4%': 4.00, 'Calcario_calcitico': 7.00, 'Sal': 0.500},
    'postura_40_a_60_semanas': {'Milho': 60.50, 'Soja_Farelo_45%': 27.00, 'Nucleo_Postura_Total_4%': 4.00, 'Calcario_calcitico': 8.00, 'Sal': 0.500},
    'postura_60_a_80_semanas': {'Milho': 60.00, 'Soja_Farelo_45%': 27.00, 'Nucleo_Postura_Total_4%': 4.00, 'Calcario_calcitico': 8.50, 'Sal': 0.500},
    'matrizes_em_reproducao': {'Milho': 58.50, 'Soja_Farelo_45%': 25.00, 'Nucleo_Postura_Presence': 6.00, 'Calcario_calcitico': 7.00, 'Sal': 0.500, 'Carne_e_Osso_45%_Farelo': 3.00}
}

# Função para calcular a quantidade total de ração para cada fase
def calcular_racao():
    fase_selecionada = combo_fase.get()
    total_racao_desejada = float(entrada_racao.get())
    ingredientes = quantidades[fase_selecionada]

    # Limpar a saída anterior
    output_display.config(state=tk.NORMAL)
    output_display.delete('1.0', tk.END)

    # Exibir a nova saída
    output_display.insert(tk.END, f'Quantidades de ingredientes para {fase_selecionada}:\n')
    for ingrediente, quantidade in ingredientes.items():
        output_display.insert(tk.END, f'{ingrediente}: {quantidade * total_racao_desejada / 100:.2f} kg\n')

    # Desativar a edição na área de saída
    output_display.config(state=tk.DISABLED)

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de Ração para Galinhas Poedeiras")

# Criar widgets
label_fase = ttk.Label(root, text="Selecione a Fase:")
combo_fase = ttk.Combobox(root, values=list(quantidades.keys()))
label_racao = ttk.Label(root, text="Quantidade Total de Ração (kg):")
entrada_racao = ttk.Entry(root)
calcular_button = ttk.Button(root, text="Calcular", command=calcular_racao)
output_display = tk.Text(root, height=10, width=50)
output_display.config(state=tk.DISABLED)  # Inicialmente desativar a edição

# Posicionar widgets na janela
label_fase.grid(row=0, column=0, padx=10, pady=10)
combo_fase.grid(row=0, column=1, padx=10, pady=10)
label_racao.grid(row=1, column=0, padx=10, pady=10)
entrada_racao.grid(row=1, column=1, padx=10, pady=10)
calcular_button.grid(row=2, column=0, columnspan=2, pady=10)
output_display.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
