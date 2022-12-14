from consumos import *

def test_barrios_top_consumo(consumos, año, clase, n=3):
    #test barrios_top_consumo
    print(f"barrios_top_consumo(consumos, {año}, {clase}, {n}")
    print(barrios_top_consumo(consumos, año, clase, n))

def test_media_consumo_edificios(consumos, clase):
    #test media_consumo_edificios
    print(f"\nmedia_consumo_edificios(consumos, {clase})")
    print(media_consumo_edificios(consumos, clase))

def test_media_consumos_de_edificio_por_tipo_edificio(consumos, año, clase):
    #test media_consumos_de_edificio_por_tipo_edificio
    print(f"\nmedia_consumos_de_edificio_por_tipo_edificio(consumos, {año}, {clase})")
    print(media_consumos_de_edificio_por_tipo_edificio(consumos, año, clase))

def test_incremento_anual_de_consumo_por_unidad(consumos, unidad=' kWh'):
    #test incremento_anual_de_consumo_por_unidad
    print(f"\nincremento_anual_de_consumo_por_unidad(consumos, {unidad})")
    print(incremento_anual_de_consumo_por_unidad(consumos, unidad))

if __name__ == '__main__':
    
    ############################# Ejercicio 1 #############################
    consumos=lee_consumos('data/consumo_energia_edificios.csv')

    print("Mostrando los 3 primeros consumos")
    for c in consumos[:3]:
        print(c)
    
    print("\nMostrando los 3 últimos consumos")
    for c in consumos[-3:]:
        print(c)
    

    ############################# Ejercicio 2 #############################
    #clase ‘ENERGIA ACTIVA’ en el año 2020 y con n = 3
    test_barrios_top_consumo(consumos, 2020, 'ENERGIA ACTIVA', 3)

    ############################# Ejercicio 3 #############################
    #clase ‘ENERGIA ACTIVA’
    test_media_consumo_edificios(consumos, 'ENERGIA REACTIVA')

    ############################# Ejercicio 4 #############################
    # Por ejemplo, si se invoca a la función con la clase de energía ‘ENERGIA REACTIVA’ y el año 2020
    test_media_consumos_de_edificio_por_tipo_edificio(consumos, 2020, 'ENERGIA REACTIVA')

    ############################# Ejercicio 5 #############################
    # Por ejemplo, si la unidad toma el valor ‘kVAr’
    test_incremento_anual_de_consumo_por_unidad(consumos, 'kVAr')