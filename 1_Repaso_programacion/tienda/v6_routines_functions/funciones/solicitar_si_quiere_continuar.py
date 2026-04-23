def solicitar_si_quiere_continuar():
    quiere_continuar = input("Quiere continuar si (s) / No (n): ")
    if(quiere_continuar == "n"):
        return False
    else:
        return True