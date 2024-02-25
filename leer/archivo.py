def mostrar_fuzz():
    with open("archivo.txt", "r") as archivo:
        Fuzz_encontrado = []
        for i in range(1, 8):
            linea_orignal = archivo.readline()
            txt = linea_orignal.lower()
            Buscar_Fuzz = "fuzz"
            if Buscar_Fuzz in txt:
                Fuzz_encontrado.append(linea_orignal)

    return Fuzz_encontrado
