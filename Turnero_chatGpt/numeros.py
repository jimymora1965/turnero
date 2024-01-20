# numeros.py

import itertools

def generar_turnos_prefijo(prefijo):
    contador = itertools.count(1)
    while True:
        yield f"{prefijo}-{next(contador)}"

def agregar_mensaje(func):
    def wrapper(*args, **kwargs):
        numero_turno = func(*args, **kwargs)
        mensaje = f"Su turno es ({numero_turno}), aguarde y será atendido."
        return mensaje
    return wrapper

generador_perfumeria = generar_turnos_prefijo("P")
generador_farmacia = generar_turnos_prefijo("F")
generador_cosmeticos = generar_turnos_prefijo("C")

@agregar_mensaje
def generar_turno_perfumeria():
    return next(generador_perfumeria)

@agregar_mensaje
def generar_turno_farmacia():
    return next(generador_farmacia)

@agregar_mensaje
def generar_turno_cosmeticos():
    return next(generador_cosmeticos)
