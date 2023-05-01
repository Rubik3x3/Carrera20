import os

numeroFin = 20
numeroAct = 0
turno = 1
turnoGanador = 0


def title():
    print(" _________                                                   ______ _______  ")
    print(" __  ____/______ ______________________ ______________ _     __|__ \__  __ \ ")
    print(" _  /     _  __ `/__  ___/__  ___/_  _ \__  ___/_  __ `/     ____/ /_  / / / ")
    print(" / /___   / /_/ / _  /    _  /    /  __/_  /    / /_/ /      _  __/ / /_/ /  ")
    print(" \____/   \__,_/  /_/     /_/     \___/ /_/     \__,_/       /____/ \____/   ")


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


while numeroAct < numeroFin:

    clear()
    title()
    print("\nNumero: ", numeroAct)
    print("Turno: Jugador ", turno)
    num = int(input("Con cuanto va a sumar? [1/2]"))
    if num == 1 or num == 2:
        numeroAct += num
        turnoGanador = turno
        if turno == 1:
            turno = 2
        else:
            turno = 1


clear()
title()
print("\nNumero: ", numeroAct)
print(f'El jugador {turnoGanador} gano!')
