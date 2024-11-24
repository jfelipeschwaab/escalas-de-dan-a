import random
import os
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

# Definir os dançarinos
adultos = ["Myllena", "Mabi", "Duda", "Thalita", "Geovana", "Alice", "Ana Ligia"]
criancas = ["Amanda", "Laura", "Rafaela"]

def gerar_escala():
    escala = {}
    adultos_rotacionados = adultos.copy()
    random.shuffle(adultos_rotacionados)  # Embaralhar para rotação

    # Domingos do mês
    domingos = ["1° Domingo", "2° Domingo", "3° Domingo", "4° Domingo"]

    # Selecionar um domingo aleatório (exceto o 1°) para a Amanda dançar
    domingo_extra_amanda = random.choice(domingos[1:])  # Escolhe entre 2°, 3° e 4° domingo

    indice_adulto = 0

    for domingo in domingos:
        if domingo == "1° Domingo":
            # 1° domingo do mês: 3 crianças e 1 adulta
            adulta = adultos_rotacionados[indice_adulto % len(adultos_rotacionados)]
            indice_adulto += 1
            escala[domingo] = {
                "Adultos": [adulta],
                "Crianças": criancas.copy()  # Todas as crianças dançam
            }
        elif domingo == domingo_extra_amanda:
            # Domingo extra em que Amanda dança: 2 adultos e Amanda
            num_adultos = 2
            participantes_adultos = []
            for _ in range(num_adultos):
                adulta = adultos_rotacionados[indice_adulto % len(adultos_rotacionados)]
                participantes_adultos.append(adulta)
                indice_adulto += 1
            escala[domingo] = {
                "Adultos": participantes_adultos,
                "Crianças": ["Amanda"]
            }
        else:
            # Domingos normais: 3 adultos
            num_adultos = 3
            participantes_adultos = []
            for _ in range(num_adultos):
                adulta = adultos_rotacionados[indice_adulto % len(adultos_rotacionados)]
                participantes_adultos.append(adulta)
                indice_adulto += 1
            escala[domingo] = {
                "Adultos": participantes_adultos,
                "Crianças": []
            }

    return escala

def gerar_pdf(escala, filename="escala_de_danca.pdf"):
    # Obter o diretório do usuário
    home = Path.home()
    # Construir o caminho para a pasta Downloads
    downloads_folder = home / "Downloads"
    # Certificar-se de que a pasta Downloads existe
    if not downloads_folder.exists():
        downloads_folder = home  # Se não existir, salvar na pasta home
    # Caminho completo do arquivo
    filepath = downloads_folder / filename

    c = canvas.Canvas(str(filepath), pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, "Escala de Dança - Mês Atual")

    y_position = height - 100
    c.setFont("Helvetica", 12)

    for domingo, participantes in escala.items():
        c.drawString(50, y_position, f"{domingo}:")
        y_position -= 20
        c.drawString(70, y_position, "Adultos:")
        y_position -= 20
        for adulto in participantes["Adultos"]:
            c.drawString(90, y_position, f"- {adulto}")
            y_position -= 15

        if participantes["Crianças"]:
            c.drawString(70, y_position, "Crianças:")
            y_position -= 20
            for crianca in participantes["Crianças"]:
                c.drawString(90, y_position, f"- {crianca}")
                y_position -= 15
        y_position -= 20  # Espaço entre os domingos

        if y_position < 100:
            c.showPage()
            y_position = height - 50

    c.save()
    return filepath  # Retornar o caminho completo do arquivo

def criar_interface():
    # Inicializar a janela principal
    janela = tk.Tk()
    janela.title("Gerador de Escala de Dança")
    janela.geometry("600x500")

    # Texto explicativo
    label = tk.Label(janela, text="Clique no botão para gerar a escala de dança.")
    label.pack(pady=10)

    # Área de texto para exibir a escala
    texto_escala = scrolledtext.ScrolledText(janela, width=70, height=20)
    texto_escala.pack(pady=10)

    # Função para o botão de gerar escala
    def botao_gerar_escala():
        escala = gerar_escala()
        # Limpar o texto anterior
        texto_escala.delete('1.0', tk.END)
        # Exibir a escala no widget de texto
        for domingo, participantes in escala.items():
            texto_escala.insert(tk.END, f"{domingo}:\n")
            texto_escala.insert(tk.END, "  Adultos:\n")
            for adulto in participantes["Adultos"]:
                texto_escala.insert(tk.END, f"    - {adulto}\n")
            if participantes["Crianças"]:
                texto_escala.insert(tk.END, "  Crianças:\n")
                for crianca in participantes["Crianças"]:
                    texto_escala.insert(tk.END, f"    - {crianca}\n")
            texto_escala.insert(tk.END, "\n")
        # Salvar a escala atual para uso no botão de salvar PDF
        janela.escala_atual = escala

    # Botão para gerar a escala
    botao_gerar = tk.Button(janela, text="Gerar Escala", command=botao_gerar_escala)
    botao_gerar.pack(pady=5)

    # Função para o botão de salvar PDF
    def botao_salvar_pdf():
        if hasattr(janela, 'escala_atual'):
            filepath = gerar_pdf(janela.escala_atual)
            messagebox.showinfo("Sucesso", f"PDF gerado com sucesso!\nSalvo em: {filepath}")
        else:
            messagebox.showwarning("Aviso", "Por favor, gere a escala primeiro.")

    # Botão para salvar a escala em PDF
    botao_salvar = tk.Button(janela, text="Salvar em PDF", command=botao_salvar_pdf)
    botao_salvar.pack(pady=5)

    # Iniciar o loop da interface
    janela.mainloop()

if __name__ == "__main__":
    criar_interface()
