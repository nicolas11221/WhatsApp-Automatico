# Install library pyautogui
import pyautogui as pg
import time as tm
import webbrowser as web

whatsapp_number = 1111111
message1 = "Example Message"
message2 = "Example Message"
message3 = "Example Message"

web.open(f"https://web.whatsapp.com/send?phone=+{whatsapp_number}")
tm.sleep(8) #Delay for messages
pg.write(f"{message} 1") # Your message
pg.press('enter') #Send

for i in range(1):
    pg.write(f"{message1} 1 \n")
    pg.write(f"{message2} 2 \n")
    pg.write(f"{message3} 3")
    pg.press('enter')
    
    print("Mensajes " +str(i+1)) #Bucle for
pass