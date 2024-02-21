def identificar_cuadrilatero(lados):
    lados = set(lados)
    num_lados = len(lados)
    
    if num_lados == 1:
        return "Es un cuadrado"
    elif num_lados == 2:
        return "Es un rectángulo"
    elif num_lados == 4:
        return "Es algún otro cuadrilátero"
    else:
        return "No es un cuadrilátero válido"

def main():
    print("Ingresa las medidas de los 4 lados del cuadrilátero:")
    lados = []
    for i in range(4):
        lado = float(input(f"Ingrese el lado {i+1}: "))
        lados.append(lado)
    
    tipo = identificar_cuadrilatero(lados)
    
    print(tipo)

if __name__ == "__main__":
    main()
