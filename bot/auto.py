import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ['+5521976005140']
while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0], 'essa mensagem foi programada por mim mãe :)',datetime.now().hour,datetime.now().minute + 2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
    