UNIDADES = ['Cero', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve']
DECENAS = ['', 'Diez', 'Veinte', 'Treinta', 'Cuarenta', 'Cincuenta', 'Sesenta', 'Setenta', 'Ochenta', 'Noventa']
CENTENAS = ['', 'Cien', 'Doscientos', 'Trescientos', 'Cuatrocientos', 'Quinientos', 'Seiscientos', 'Setecientos', 'Ochocientos', 'Novecientos']

def convertir_miles(numero):
    if numero < 10:
        return UNIDADES[numero]
    elif numero < 100:
        if numero % 10 == 0:
            return DECENAS[numero // 10]
        else:
            return DECENAS[numero // 10] + ' y ' + UNIDADES[numero % 10]
    elif numero < 1000:
        if numero % 100 == 0:
            return CENTENAS[numero // 100]
        else:
            return CENTENAS[numero // 100] + ' ' + convertir_miles(numero % 100)

def convertir_numero_a_letras(numero):
    if numero < 1000:
        return convertir_miles(numero)
    elif numero < 1000000:
        if numero % 1000 == 0:
            return convertir_miles(numero // 1000) + ' Mil'
        else:
            return convertir_miles(numero // 1000) + ' Mil ' + convertir_miles(numero % 1000)
    elif numero < 1000000000:
        if numero % 1000000 == 0:
            return convertir_miles(numero // 1000000) + ' Millones'
        else:
            return convertir_miles(numero // 1000000) + ' Millones ' + convertir_numero_a_letras(numero % 1000000)
    elif numero < 1000000000000:
        if numero % 1000000000 == 0:
            return convertir_miles(numero // 1000000000) + ' Mil Millones'
        else:
            return convertir_miles(numero // 1000000000) + ' Mil Millones ' + convertir_numero_a_letras(numero % 1000000000)
    elif numero < 1000000000000000:
        if numero % 1000000000000 == 0:
            return convertir_miles(numero // 1000000000000) + ' Billones'
        else:
            return convertir_miles(numero // 1000000000000) + ' Billones ' + convertir_numero_a_letras(numero % 1000000000000)
    else:
        return 'Número demasiado grande'

numero = int(input("Introduce un número: "))
print(convertir_numero_a_letras(numero))
