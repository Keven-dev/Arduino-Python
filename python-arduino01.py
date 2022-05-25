from pyfirmata import Arduino
from random import randint
from time import localtime, sleep

Uno = Arduino('COM6')
print('Olá Mundo!')

ledVermelho = 3
ledAmarelo = 5
ledVerde = 6
buzzer = 10

while True:
    delay = randint(1, 10)

    Uno.digital[buzzer].write(1)
    sleep(0.1)
    Uno.digital[buzzer].write(0)
    Uno.digital[ledVermelho].write(1)
    Uno.digital[ledAmarelo].write(1)
    Uno.digital[ledVerde].write(1)
    tempo_ligado = localtime()
    print('Led ligado')
    print('Hora {}:{}:{}'.format(tempo_ligado[3], tempo_ligado[4], tempo_ligado[5]))
    sleep(delay)

    Uno.digital[buzzer].write(1)
    sleep(0.1)
    Uno.digital[buzzer].write(0)
    Uno.digital[ledVermelho].write(0)
    Uno.digital[ledAmarelo].write(0)
    Uno.digital[ledVerde].write(0)
    tempo_desligado = localtime()
    print('Led desligado')
    print('Hora {}:{}:{}'.format(tempo_desligado[3], tempo_desligado[4], tempo_desligado[5]))
    print('=' * 20)
    sleep(delay)
