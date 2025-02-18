"""
Agendamento de desligamento
Crie duas funções em python para agendar 
o desligamento do computador em uma hora e meia hora.

"""

import os

# 1 - Desligar o computador

# os.system("shutdown /s") # Desliga o computador em 60s
# os.system("shutdown /s /t 0") # Desliga o computador Imediatamente
# os.system("shutdown now")


# 2 - Cancelar desligamento
# os.system("shutdown /a")


def turn_off_one_hour(): # desliga em 1h
    os.system("shutdown /s /t 3600")
    
def turn_off_half_an_hour():
    os.system("shutdown /s /t 1800") # desliga em 30m
    
def calcel_shutdown(): # cancela o desligamento
    os.system("shutdown /a")
    
turn_off_one_hour()
calcel_shutdown()