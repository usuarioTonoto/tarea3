def es_simetrica(matriz):
    """
    UWU hijos de puta me dejaron la mas dificil
    esos bastardos me mintieron
    """
    if len(matriz) != len(matriz[0]):
        return False
    for i in range(len(matriz)-1):
        for j in range(len(matriz[0])-1):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

