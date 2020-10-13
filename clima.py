from tkinter import *
import requests
#db48b9e563280c4e7f50bc04c850fd8e
#api.openweathermap.org/data/2.5/weather?q={city name}

def mostrar_clima(clima):
	nombre_ciudad = clima["name"]
	desc = clima["weather"][0]["description"]
	temp = clima["main"]["temp"]

	ciudad["text"] = nombre_ciudad
	temperatura["text"] = str(int(temp)) + "ªC"
	descripcion["text"] = desc
 
def clima_JSON(ciudad):
	API_key = "db48b9e563280c4e7f50bc04c850fd8e"
	URL = "https://api.openweathermap.org/data/2.5/weather"
	parametros = {"APPID" : API_key, "q" : ciudad, "units" : "metric", "lang" : "es"}
	response = requests.get(URL, params=parametros)
	clima = response.json()


	mostrar_clima(clima)

ventana = Tk()
ventana.geometry("350x350") 

texto_ciudad = Entry(ventana, font=("Courier", 20, "normal"), justify= "center")
texto_ciudad.pack(padx= 30, pady= 30)

obtener_clima = Button(ventana, text="Obtener Clima", command= lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(font=("Courier", 20, "normal"))
ciudad.pack(padx = 20, pady=20)

temperatura = Label(font=("Courier", 50, "normal"))
temperatura.pack(padx = 10, pady=10)

descripcion = Label(font=("Courier", 20, "normal"))
descripcion.pack(padx = 10, pady=10)

ventana.mainloop() 