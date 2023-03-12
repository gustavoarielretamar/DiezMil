import random

#%% TIRAN d DADOS Y GUARDA LOS VALORES:
def tirar_cubilete(d, debug = False):
    dados = []
    contador = 0
    while contador < d:
        dado = random.randint(1, 6)
        dados.append(dado)
        contador = contador + 1
    if debug:
        print (dados)
    return dados
#%% CUENTA LA CANTIDAD DE "ELEMENTOS":
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
#%% CUENTA LA CANTIDAD DE 1:
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
#%% CUETA LA CANTUDAD DE 5:
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
#%% 5
def puntos_totales(unos, cincos, debug = False):
    puntosTotales = unos + cincos
    if debug:
        print (puntosTotales)
    return puntosTotales
#%% JUEGA UNA RONDA COMPLETA CON k jugadores
def jugar_ronda(k, debug = False):
    contador=0
    tabla = []
    while contador < k:
        lista_dados = tirar_cubilete(d)
        cantidad_de_unos = cuantos_hay (1, lista_dados)
        cantidad_de_cincos = cuantos_hay (5, lista_dados)
        puntosUnos = puntos_por_unos(cantidad_de_unos)
        puntosCincos = puntos_por_cincos(cantidad_de_cincos)
        puntos = puntos_totales(puntosUnos, puntosCincos)
        tabla.append(puntos)
        contador = contador +1
    if debug:
        print (tabla)
    return tabla
# %% ACUMULAR TODOS LOS PUNTOS:
def acumular_puntos(puntajes_acumulados, puntajes_ronda, debug = False):
    for i in range(0, len(puntajes_acumulados)):
        puntajes_acumulados[i] = puntajes_acumulados[i] + puntajes_ronda[i]
    if debug:
        print(puntajes_acumulados)
    return puntajes_acumulados
# %% BUSCAR SI HAY GANADORES:
def hay_10_mil(puntajes, debug = False):
    ganador = False
    for i in range(len(puntajes)):
        if puntajes[i]  >= 10000:
            ganador = True
    if debug: 
        print(ganador)
    return ganador
# %% JUGAR PARTIDA:
def jugar_partida(k, debug = False):
    score = [0]*k
    partidas = 1
    while not hay_10_mil(score):
        tabla = jugar_ronda(k)
        score = acumular_puntos(score, tabla)
        partidas += 1
    if debug:
        print(score)
        print (partidas)
    return partidas
# %% PROMEDIOS:
def promedio(Nrep, debug = False):
    cant_rondas = [0]*Nrep
    i = 1
    while i < Nrep:
        partidas = jugar_partida(k)
        cant_rondas.append(partidas)
        i += 1
    promedio = sum(cant_rondas) / Nrep
    promedio = int(promedio)
    if debug:
        print (promedio)
    return promedio
# %% LISTA DE PARTIDAS JUGADAS PARA LLEGAR A 10000:
def lista(Nrep, debug = False):
    cant_rondas = [0]*Nrep
    i = 1
    while i < Nrep:
        partidas = jugar_partida(k)
        cant_rondas.append(partidas)
        i += 1
    if debug:
        print (cant_rondas)
    return cant_rondas
# %% CHANCES:
def dame_chances(resultados, cantidad_maxima, debug = False):
    i = 0
    meSirve = 0
    while i<len(resultados):
        if resultados[i] <= cantidad_maxima:
            meSirve = meSirve + 1
        i += 1
    chances= meSirve/len(resultados)
    if debug:
        print (chances)
    return chances
# %% PARAMETROS:
d = 5
k = 20
Nrep = 10000
cantidad_maxima = 18
resultados = lista(Nrep)
# %% LLAMADAS:
# tirada = tirar_cubilete(d)
# cantidad_de_unos = cuantos_hay (1, tirada)
# cantidad_de_cincos = cuantos_hay (5, tirada)
# puntosUnos = puntos_por_unos(cantidad_de_unos)
# puntosCincos = puntos_por_cincos(cantidad_de_cincos)
# puntaje = puntos_totales(puntosUnos, puntosCincos)
# ronda = jugar_ronda(5)
# acumulados = [10, 10, 10, 10, 10]
# acumular_puntos(acumulados, ronda, True)
# hay_10_mil(t1, True)
# jugar_partida(k, True)
# promedio(Nrep, True)
dame_chances(resultados, cantidad_maxima, True)
