import customtkinter as ctk

def calcular_imc(peso, altura):
    """Função para calcular o IMC"""
    return peso / (altura * altura)

def determinar_categoria(imc):
    """Função para determinar a categoria e a cor correspondente ao IMC"""
    if imc < 17:
        return 'Muito abaixo do peso', '#FFFE01'
    elif 17 <= imc < 18.5:
        return 'Abaixo do peso', '#D8FF6D'
    elif 18.5 <= imc < 25:
        return 'Peso normal', '#20FF00'
    elif 25 <= imc < 30:
        return 'Sobrepeso', '#FFAA00'
    elif 30 <= imc < 35:
        return 'Obesidade I', '#FF7B02'
    elif 35 <= imc < 40:
        return 'Obesidade II (severa)', '#FF4B00'
    else:
        return 'Obesidade III (mórbida)', '#FF0B00'

def atualizar_campos(imc, categoria, cor_texto, campo_resultado, campo_categoria):
    """Função para atualizar os campos de resultado e categoria"""
    campo_resultado.configure(state="normal")  # Permite editar o campo
    campo_resultado.delete(0, ctk.END)  # Limpa o campo de resultado
    campo_resultado.insert(0, f'{imc:.2f}')  # Insere o valor do IMC no campo
    
    campo_categoria.configure(state="normal")  # Permite editar o campo
    campo_categoria.delete(0, ctk.END)  # Limpa o campo de categoria
    campo_categoria.insert(0, categoria)  # Insere a categoria no campo
    
    # Alterando a cor do texto da categoria
    campo_categoria.configure(text_color=cor_texto)  # Aplica a cor ao texto da categoria
    
    campo_resultado.configure(state="disabled")  # Desabilita o campo após inserir o valor
    campo_categoria.configure(state="disabled")  # Desabilita o campo após inserir o valor

class CalculadoraIMCApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x400')
        self.root.minsize(350, 350)
        self.root.configure(padx=20, pady=20, bg_color='#6438FF')  # Fundo roxo para a janela
        self.root.title('Calculadora IMC')

        # Fontes
        self.fonte_texto_principal = ctk.CTkFont('Arial', 18, 'bold')
        self.fonte_padrao = ctk.CTkFont('Arial', 14, 'bold')

        # Componentes da interface
        self.criar_widgets()

    def criar_widgets(self):
        """Função para criar os widgets"""
        texto_principal = ctk.CTkLabel(self.root, text='Melhor Saúde', font=self.fonte_texto_principal, text_color='#FFF91F')
        texto_principal.grid(row=0, column=0, columnspan=2, pady=(30, 10))

        texto_principal_sub = ctk.CTkLabel(self.root, text='Calcule seu IMC e tome decisões mais saudáveis', font=self.fonte_padrao)
        texto_principal_sub.grid(row=1, column=0, columnspan=2, pady=(15))

        # Entrada de peso
        self.textinsideblock = self.criar_entrada('Digite seu peso:', 'PESO', 2)
        
        # Entrada de altura
        self.textinsideblock_two = self.criar_entrada('Digite sua altura:', 'ALTURA', 3)
        
        # Botão para calcular o IMC
        botao_calcular = ctk.CTkButton(self.root, text="Obter resultado", command=self.calcular_dados, font=self.fonte_padrao, corner_radius=20, text_color='#FFF9BF', fg_color='#6438FF')
        botao_calcular.grid(row=4, column=0, columnspan=2, pady=15)

        # Labels e campos para exibir o resultado
        self.campo_resultado = self.criar_entrada('Resultado: ', 'IMC', 5, disabled=True)
        self.campo_categoria = self.criar_entrada('Categoria: ', 'Categoria', 6, disabled=True, width=160)

    def criar_entrada(self, texto_label, texto_placeholder, linha, disabled=False, width=150):
        """Função auxiliar para criar campos de entrada"""
        label = ctk.CTkLabel(self.root, text=texto_label, font=self.fonte_padrao)
        label.grid(row=linha, column=0, pady=5, sticky="w", padx=20)

        entry = ctk.CTkEntry(self.root, placeholder_text=texto_placeholder, corner_radius=10, width=width)
        entry.grid(row=linha, column=1, pady=5, padx=20)
        if disabled:
            entry.configure(state="disabled")  # Deixa o campo desabilitado

        return entry

    def calcular_dados(self):
        """Função chamada quando o botão for pressionado"""
        try:
            peso = float(self.textinsideblock.get())
            altura = float(self.textinsideblock_two.get())
        except ValueError:
            return  # Se os valores não forem numéricos, não faz nada

        # Calculando o IMC
        imc = calcular_imc(peso, altura)
        print(f'Com base nos seus dados o seu IMC é: {imc:.2f}')
        
        # Determinando a categoria e cor correspondente
        categoria, cor_texto = determinar_categoria(imc)
        
        # Atualizando os campos de resultado e categoria
        atualizar_campos(imc, categoria, cor_texto, self.campo_resultado, self.campo_categoria)

# Iniciando a interface
if __name__ == "__main__":
    ctk.set_default_color_theme('blue')
    ctk.set_appearance_mode('dark')
    
    janela = ctk.CTk()
    app = CalculadoraIMCApp(janela)
    janela.mainloop()