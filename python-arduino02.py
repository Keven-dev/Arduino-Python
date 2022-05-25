from pyfirmata import Arduino
from time import sleep

Uno = Arduino('COM6')
print('Olá Mundo!')

ledVermelho = 3
ledAmarelo = 5
ledVerde = 6
buzzer = 10


def liga_ledVerde():
    Uno.digital[buzzer].write(1)
    sleep(0.03)
    Uno.digital[buzzer].write(0)
    Uno.digital[ledVerde].write(1)
    sleep(0.5)
    Uno.digital[ledVerde].write(0)


def liga_ledAmarelo():
    Uno.digital[buzzer].write(1)
    sleep(0.03)
    Uno.digital[buzzer].write(0)
    Uno.digital[ledAmarelo].write(1)
    sleep(0.5)
    Uno.digital[ledAmarelo].write(0)


def liga_ledVermelho():
    Uno.digital[buzzer].write(1)
    sleep(0.03)
    Uno.digital[buzzer].write(0)
    Uno.digital[ledVermelho].write(1)
    sleep(0.5)
    Uno.digital[ledVermelho].write(0)


while True:
    liga_ledVerde()
    sleep(0.5)
    liga_ledAmarelo()
    sleep(0.5)
    liga_ledVermelho()
    sleep(0.5)
    liga_ledVermelho()
    sleep(0.5)
    liga_ledAmarelo()
    sleep(0.5)
    liga_ledVerde()
    sleep(0.5)
