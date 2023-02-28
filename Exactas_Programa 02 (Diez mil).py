import random

#%% 1
cantidad_dados = 5
def tirar_cubilete(debug = False):
    dados = []
    contador = 0
    while contador < cantidad_dados:
        dado = random.randint(1, 6)
        dados.append(dado)
        contador = contador + 1
    if debug:
        print (dados)
    return dados

# lista_dados = tirar_cubilete()


#%% 2
def cuantos_hay (elemento, lista, debug = False):
    contador = 0
    cantidad = 0
    while contador < len(lista):
        if lista[contador] == elemento:
            cantidad = cantidad + 1
        contador = contador + 1
    if debug:
        print (cantidad)
    return cantidad

# cantidad_de_unos = cuantos_hay (1, lista_dados)
# cantidad_de_cincos = cuantos_hay (5, lista_dados)


#%% 3 ESTE CODIGO LO ESCRIBÍ YO
def puntos_por_unos (lista_dados, debug = False):
    puntajeUnos = 0
    if lista_dados >= 5:
        puntajeUnos = 10000
        lista_dados = lista_dados - 5
    elif lista_dados >=4:
        puntajeUnos = 1100
        lista_dados = lista_dados - 4
    elif lista_dados >= 3:
        puntajeUnos = 1000
        lista_dados = lista_dados - 3
    else:
        puntajeUnos = lista_dados * 100
    if debug:
        print (puntajeUnos)
    return puntajeUnos

# puntosUnos = puntos_por_unos(cantidad_de_unos)


#%% 4 ESTE CODIGO NOS PRESENTARON EN EL PIZZARRON
def puntos_por_cincos (lista_dados, debug = False):   
    puntajeCincos = 0
    if lista_dados < 3:
        puntajeCincos = lista_dados * 100
    elif lista_dados == 3:
        puntajeCincos = 1000
    elif lista_dados == 4:
        puntajeCincos = 1100
    else :
        puntajeCincos = 10000
    if debug:
        print (puntajeCincos)
    return puntajeCincos
    
# puntosCincos = puntos_por_cincos(cantidad_de_cincos)


#%% 5
def puntos_totales(unos, cincos, debug = False):
    puntosTotales = unos + cincos
    if debug:
        print (puntosTotales)
    return puntosTotales
    
# puntaje = puntos_totales(puntosUnos, puntosCincos)


#%% 6
#k es el numero de jugadores
def jugar_ronda(k):
    contador=0
    tabla = []
    while contador < k:
        lista_dados = tirar_cubilete()
        cantidad_de_unos = cuantos_hay (1, lista_dados)
        cantidad_de_cincos = cuantos_hay (5, lista_dados)
        puntosUnos = puntos_por_unos(cantidad_de_unos)
        puntosCincos = puntos_por_cincos(cantidad_de_cincos)
        puntos = puntos_totales(puntosUnos, puntosCincos)
        tabla.append(puntos)
        contador = contador +1
    print (tabla)
    return tabla

jugar_ronda(5)