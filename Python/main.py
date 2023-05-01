import os

numeroFin = 0
sumas = 0


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


clear()
title()

numeroFin = int(input("Ingrese el número al que hay que llegar: "))
sumas = int(input("Ingrese el número máximo que se puede sumar: "))

clear()
title()
