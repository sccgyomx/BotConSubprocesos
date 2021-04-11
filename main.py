import webbrowser
import subprocess
import tkinter as tk
import time

url = [
    'https://www.it-swarm-es.com/es/python/python-funcion-para-convertir-segundos-en-minutos-horas-y-dias/970796451/',
    'https://www.sublimetext.com/3',
    'https://docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/widget-label-etiqueta-de-texto/',
    'https://es.stackoverflow.com/questions/159290/incrustar-comandos-de-windows-o-cmd-en-un-script-de-python',
    'https://rico-schmidt.name/pymotw-3/cmd/',
    'https://store.brave.com/#/'
]

webbrowser.register('brave', None, webbrowser.BackgroundBrowser(
    'C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe'))
bandera = 0


class App:

    def __init__(self, master):
        self.ventana = master
        self.estado = ""
        self.proceso = subprocess
        self.dibujarLabel()
        self.dibujarBoton()

    def dibujarLabel(self):
        self.lblNombre = tk.Label(self.ventana, font=15, foreground="white", background="#343434", text="Brave").place(
            x=150, y=80)
        self.lblAviso = tk.Label(self.ventana, font=15, foreground="white", background="#343434",
                                 text=self.estado).place(x=150, y=100)

    def dibujarBoton(self):
        self.iniciarBoton = tk.Button(self.ventana, text="Iniciar Bot", background="#499C54",
                                      foreground="#343434", relief="flat", command=self.ejecutar).place(x=100, y=300,
                                                                                                        width=90)
        self.terminarBoton = tk.Button(self.ventana, text="Terminar Bot", background="#FF5340",
                                       foreground="#343434", relief="flat", command=self.kill).place(x=200, y=300,
                                                                                                     width=90)

    def ejecutar(self):
        self.estado = "Bot Iniciado"
        self.dibujarLabel()
        iniciar()

    def kill(self):
        self.estado = "Bot Detenido"
        self.dibujarLabel()
        # subprocess.run('taskkill /IM notepad.exe', shell=True)


def iniciar():
    for i in url:
        #webbrowser.get('brave').open(url[0])
        time.sleep(10)
        #subprocess.run('taskkill /IM brave.exe', shell=True)
        print(i)
    iniciar()


root = tk.Tk()
root.title("CRUD Con TKinter y MySQL")
root.geometry("400x400")
root.config(background="#343434")
application = App(root)
root.mainloop()
