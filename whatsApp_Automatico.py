# Install library pyautogui
import pyautogui as pg
import time as tm
import webbrowser as web

index = 0
whatsapp_number = 56953955540
messages = ["Message", "Message", "Message", "Message"]

web.open(f"https://web.whatsapp.com/send?phone=+{whatsapp_number}")
tm.sleep(8) #Delay for messages

for message in messages:
    if message:
        pg.write(f"{message} \n")
        pg.press('enter')
        index += 1
        print(f"{message} {index}")
pass