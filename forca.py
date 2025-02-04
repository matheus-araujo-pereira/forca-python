import tkinter as tk
from tkinter import messagebox

class JogoDaForca:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Jogo da Forca")
        self.janela.configure(bg="#1E1E1E")
        self.janela.geometry("500x600")
        
        self.palavra = ""
        self.palavra_descoberta = []
        self.letras_erradas = []
        self.tentativas = 6
        self.desenho_forca = [
            "Cabeça",
            "Corpo",
            "Perna Esquerda",
            "Perna Direita",
            "Braço Esquerdo",
            "Braço Direito"
        ]
        
        self.frame_entrada_palavra = tk.Frame(self.janela, bg="#1E1E1E")
        self.frame_entrada_palavra.pack(pady=20)
        
        self.label_instrucoes = tk.Label(self.frame_entrada_palavra, text="Digite a palavra para o jogo:", 
                                         font=("Arial", 14, "bold"), bg="#1E1E1E", fg="#FFFFFF")
        self.label_instrucoes.grid(row=0, column=0, pady=10)
        
        self.entrada_palavra = tk.Entry(self.frame_entrada_palavra, font=("Arial", 14), width=15, justify="center")
        self.entrada_palavra.grid(row=1, column=0, pady=10)
        
        self.botao_iniciar = tk.Button(self.frame_entrada_palavra, text="Iniciar Jogo", font=("Arial", 12, "bold"), 
                                       bg="#2D89EF", fg="#FFFFFF", relief="flat", 
                                       activebackground="#1B5D9B", activeforeground="#FFFFFF", 
                                       highlightbackground="#000000", highlightthickness=3, bd=5,
                                       command=self.iniciar_jogo)
        self.botao_iniciar.grid(row=2, column=0, pady=10)
        
        self.janela.mainloop()

    def iniciar_jogo(self):
        palavra_digitada = self.entrada_palavra.get().strip().upper()
        
        if not palavra_digitada:
            messagebox.showwarning("Aviso", "Por favor, digite uma palavra!")
            return
        
        self.palavra = palavra_digitada
        self.palavra_descoberta = ["_" for _ in self.palavra]
        self.letras_erradas = []
        self.tentativas = 6
        
        self.frame_entrada_palavra.pack_forget()

        self.frame_forca = tk.Frame(self.janela, bg="#1E1E1E")
        self.frame_forca.pack(pady=20)
        
        self.label_palavra = tk.Label(self.janela, text=" ".join(self.palavra_descoberta), font=("Arial", 20, "bold"), bg="#1E1E1E", fg="#FFFFFF")
        self.label_palavra.pack()
        
        self.label_tentativas = tk.Label(self.janela, text=f"Tentativas restantes: {self.tentativas}", font=("Arial", 14, "bold"), bg="#1E1E1E", fg="#FFFFFF")
        self.label_tentativas.pack()
        
        self.label_erradas = tk.Label(self.janela, text="Letras erradas: ", font=("Arial", 12, "bold"), bg="#1E1E1E", fg="#FFFFFF")
        self.label_erradas.pack()
        
        self.botao_tentar = tk.Button(self.janela, text="Tentar", font=("Arial", 12, "bold"), bg="#2D89EF", fg="#FFFFFF", relief="flat", 
                                      activebackground="#1B5D9B", activeforeground="#FFFFFF", highlightbackground="#000000", highlightthickness=3, bd=5,
                                      command=self.tentar_letra)
        self.botao_tentar.pack(pady=10)
        
        self.entrada_letra = tk.Entry(self.janela, font=("Arial", 12), width=5, justify="center")
        self.entrada_letra.pack(pady=10)

        self.canvas_forca = tk.Canvas(self.janela, width=200, height=250, bg="#1E1E1E")
        self.canvas_forca.pack(pady=20)

    def tentar_letra(self):
        letra = self.entrada_letra.get().upper()
        self.entrada_letra.delete(0, tk.END)
        
        if letra in self.letras_erradas or letra in self.palavra_descoberta:
            return
        
        if letra in self.palavra:
            for i in range(len(self.palavra)):
                if self.palavra[i] == letra:
                    self.palavra_descoberta[i] = letra
            self.label_palavra.config(text=" ".join(self.palavra_descoberta))
            
            if "_" not in self.palavra_descoberta:
                messagebox.showinfo("Você venceu!", "Parabéns! Você adivinhou a palavra!")
                self.janela.quit()
        else:
            self.letras_erradas.append(letra)
            self.tentativas -= 1
            self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas}")
            self.label_erradas.config(text=f"Letras erradas: {', '.join(self.letras_erradas)}")
            self.exibir_forca()
            
            if self.tentativas == 0:
                messagebox.showinfo("Você perdeu", f"Você perdeu! A palavra era {self.palavra}")
                self.janela.quit()

    def exibir_forca(self):
        self.canvas_forca.delete("all")
        
        if self.tentativas <= 5:
            self.canvas_forca.create_oval(75, 20, 125, 70, outline="white", width=2)
        if self.tentativas <= 4:
            self.canvas_forca.create_line(100, 70, 100, 130, fill="white", width=2)
        if self.tentativas <= 3:
            self.canvas_forca.create_line(100, 130, 50, 190, fill="white", width=2)
        if self.tentativas <= 2:
            self.canvas_forca.create_line(100, 130, 150, 190, fill="white", width=2)
        if self.tentativas <= 1:
            self.canvas_forca.create_line(100, 90, 50, 130, fill="white", width=2)
        if self.tentativas <= 0:
            self.canvas_forca.create_line(100, 90, 150, 130, fill="white", width=2)

if __name__ == "__main__":
    JogoDaForca()
