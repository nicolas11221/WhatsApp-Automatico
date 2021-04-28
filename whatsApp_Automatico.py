
#Debe Instalar la libreria 
# pip install pyautogui

import pyautogui as pg
import time as tm
import webbrowser as web

# Aqui Deben Reemplazar NUMERO Por El Numero Al Cual Desean Enviar El Mensaje
#Ejemplo
#web.open("https://web.whatsapp.com/send?phone=+56912312312")

web.open("https://web.whatsapp.com/send?phone=+NUMERO")
tm.sleep(8) #Tiempo De Espera Para Ejecutar Mensajes,
            #Por La Demora De La Carga De Pagina
pg.write("Prueba De Mensajes Numero 1") #Mensaje 
pg.press('enter') #Boton Apretado Automatico

for i in range(1):
    pg.write("Mensaje Numero 1 \n")
    pg.write("Mensaje Numero 2 \n")
    pg.write("Mensaje Numero 3")
    pg.press('enter')
    
    print("Mensajes " +str(i+1)) #Contador De Mensajes
pass