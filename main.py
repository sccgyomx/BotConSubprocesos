import subprocess
import time
import webbrowser
from PIL import ImageTk, Image
import tkinter as tk
import schedule
import threading
import random

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
cease_continuous_run = threading.Event()

class App:

    def __init__(self, master):
        self.stop_run_continuously = run_continuously()
        self.stop_run_continuously.set()
        self.ventana = master
        self.estado = ""
        self.dibujarLabel()
        self.dibujarBoton()

    def dibujarLabel(self):
        self.lblAviso = tk.Label(self.ventana, font=15, foreground="white", background="#343434",
                                 text=self.estado).place(x=150, y=405)

    def dibujarBoton(self):
        self.iniciarBoton = tk.Button(self.ventana, text="Iniciar Bot", background="#499C54",
                                      foreground="#343434", relief="flat",font= 15, command=self.ejecutar).place(x=500, y=400,
                                                                                                        width=100)
        self.terminarBoton = tk.Button(self.ventana, text="Terminar Bot", background="#FF5340",
                                       foreground="#343434", relief="flat",font= 15, command=self.kill).place(x=620, y=400,
                                                                                                     width=100)


    def ejecutar(self):
        self.estado = "Bot Iniciado"
        self.dibujarLabel()
        schedule.every(5).minutes.do(iniciar)
        self.stop_run_continuously = run_continuously()

    def kill(self):
        self.estado = "Bot Detenido"
        self.dibujarLabel()
        self.stop_run_continuously.set()
        # subprocess.run('taskkill /IM notepad.exe', shell=True)


def iniciar():
    i= random.randint(0,5)
    if (variableGlobal.bandera==True):
        webbrowser.get('brave').open(url[i])
        #print(variableGlobal.bandera)
        variableGlobal.bandera=False
    else:
        subprocess.run('taskkill /IM brave.exe', shell=True)
        #print(variableGlobal.bandera)
        variableGlobal.bandera=True


class variableGlobal:
    bandera=True



def run_continuously(interval=1):
    """Continuously run, while executing pending jobs at each
    elapsed time interval.
    @return cease_continuous_run: threading. Event which can
    be set to cease continuous run. Please note that it is
    *intended behavior that run_continuously() does not run
    missed jobs*. For example, if you've registered a job that
    should run every minute and you set a continuous run
    interval of one hour then your job won't be run 60 times
    at each interval but only once.
    """
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


root = tk.Tk()
root.title("Bot Brave")
root.geometry("800x500")
root.config(background="#343434")
root.resizable(width=False, height=False)
c = tk.Canvas(root, width=800, height=400, background ="#343434",highlightthickness=0)
c.pack()
img = ImageTk.PhotoImage(Image.open(r"img/brave-logo-monotone-reversed.png"))
c.create_image( 400 , 200, image=img,anchor="c")
application = App(root)
root.mainloop()
#application.kill()
