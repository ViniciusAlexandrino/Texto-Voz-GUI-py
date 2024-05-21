import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

# Inicializa a janela principal
root = Tk()
root.title("Texto para Voz")  # Define o título da janela
root.geometry("900x450")  # Define o tamanho da janela
root.resizable(False, False)  # Desabilita a redimensionamento da janela
root.configure(bg="#305065")  # Define a cor de fundo da janela

# Inicializa o motor de conversão de texto para fala
engine = pyttsx3.init()

# Função para converter texto em fala
def speaknow():
    text = text_area.get(1.0, END)  # Obtém o texto da área de texto
    gender = gender_combobox.get()  # Obtém o gênero selecionado
    speed = speed_combobox.get()  # Obtém a velocidade selecionada
    voices = engine.getProperty('voices')  # Obtém as vozes disponíveis

    if text.strip():  # Verifica se o texto não está vazio
        # Define a voz com base no gênero selecionado
        if gender == "Masculino":
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)

        # Define a velocidade de fala com base na seleção do usuário
        if speed == "Rápido":
            engine.setProperty('rate', 250)
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        
        engine.say(text)  # Converte o texto em fala
        engine.runAndWait()  # Executa a conversão

# Configuração do cabeçalho
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)

# Rótulo do cabeçalho
Label(Top_frame, text="TEXTO PARA VOZ", font="arial 20 bold", bg="white", fg="black").place(x=100, y=30)

# Área de texto onde o usuário digita o texto a ser convertido
text_area = Text(root, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

# Rótulos para opções de voz e velocidade
Label(root, text="VOZ", font="arial 15 bold", bg="#305065", fg="white").place(x=580, y=160)
Label(root, text="VELOCIDADE", font="arial 15 bold", bg="#305065", fg="white").place(x=730, y=160)

# Combobox para seleção de gênero (voz)
gender_combobox = Combobox(root, values=['Masculino', 'Feminino'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Masculino')  # Define valor padrão

# Combobox para seleção de velocidade de fala
speed_combobox = Combobox(root, values=['Rápido', 'Normal', 'Lento'], font="arial 14", state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')  # Define valor padrão

# Botão para iniciar a conversão de texto para fala
btn = Button(root, text="Fale", width=10, font="arial 14 bold", command=speaknow)
btn.place(x=550, y=280)

# Inicia o loop principal da interface gráfica
root.mainloop()
