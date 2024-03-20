def generar_cuadrado_espiral(n):
    # Inicializar la matriz
    matriz = [[0] * n for _ in range(n)]
    valor = 1
    limite_superior = 0
    limite_inferior = n - 1
    limite_izquierdo = 0
    limite_derecho = n - 1
    while valor <= n * n:
        # Rellenar la fila superior
        for i in range(limite_izquierdo, limite_derecho + 1):
            matriz[limite_superior][i] = valor
            valor += 1
        limite_superior += 1      
        # Rellenar la columna derecha
        for i in range(limite_superior, limite_inferior + 1):
            matriz[i][limite_derecho] = valor
            valor += 1
        limite_derecho -= 1        
        # Rellenar la fila inferior
        for i in range(limite_derecho, limite_izquierdo - 1, -1):
            matriz[limite_inferior][i] = valor
            valor += 1
        limite_inferior -= 1      
        # Rellenar la columna izquierda
        for i in range(limite_inferior, limite_superior - 1, -1):
            matriz[i][limite_izquierdo] = valor
            valor += 1
        limite_izquierdo += 1
    max_valor_length = len(str(n * n))
    spaces = " " * ((max_valor_length + 1) * (n - 1) // 2)
    for fila in matriz:
        print(spaces + " ".join(map(lambda x: f"{x:>{max_valor_length}}", fila)))
tamaño = int(input("Ingrese el tamaño del cuadrado en espiral: "))
generar_cuadrado_espiral(tamaño)