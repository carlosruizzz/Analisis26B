import tkinter as tk
#import matplotlib.pylot as plt

x = [3, 4, 5, 6, 7]
y = [10, 11, 14, 16, 18]

#plt.plot(x,y) grafica de lineas
plt.scatter(x,y)
#plt.bar(x,y) grafica de barras
plt.title("mi mprimera graifica")
plt.xlabvel("eje x")
plt.ylabel("eje y")
plt.show()

def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "mundo"
    lbl.config(text = f"Hola {nombre}")


root = tk.Tk()
root.title("Saludador")
root.geometry("360x220")

lbl = tk.Label(root, text="eh compa,Escribe tu nombre y presiona el boton", background="pink", foreground="purple")
lbl.pack(pady=10)
entrada = tk.Entry(root, background="gray")
entrada.pack(pady=10)
bot = tk.Button(root, text="Saludar", command=saludar)
bot.pack(pady=10)

root.mainloop()