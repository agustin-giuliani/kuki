# -*- coding: utf-8 -*-

import os

from brain.learning.memory import Memory
from brain.learning.memory_integrator import MemoryIntegrator


# --------------------------------
# LIMPIAR ARCHIVO DE PRUEBA
# --------------------------------

# Eliminamos el archivo anterior para que
# cada ejecución del test empiece desde cero.
if os.path.exists(
    "data/test_memory_integrator.json"
):

    os.remove(
        "data/test_memory_integrator.json"
    )


# --------------------------------
# CREAR COMPONENTES
# --------------------------------

# Creamos una instancia de Memory
# utilizando un archivo exclusivo para pruebas.
memoria = Memory(
    "data/test_memory_integrator.json"
)

# Creamos el integrador y le pasamos Memory.
integrador = MemoryIntegrator(
    memoria
)


print("--- MEMORY INTEGRATOR ---")


# --------------------------------
# DATO UNICO
# --------------------------------

print()
print("Guardar nombre:")

print(
    integrador.integrar(
        "nombre",
        "agustin",
        "dato_unico",
        "identidad"
    )
)


# Mostramos cómo quedó guardado.
print(
    "Nombre:",
    memoria.recordar(
        "nombre"
    )
)


# --------------------------------
# ACTUALIZAR DATO UNICO
# --------------------------------

print()
print("Actualizar nombre:")

print(
    integrador.integrar(
        "nombre",
        "agustin giuliani",
        "dato_unico",
        "identidad"
    )
)


# Comprobamos que el valor anterior
# haya sido reemplazado por el nuevo.
print(
    "Nombre actualizado:",
    memoria.recordar(
        "nombre"
    )
)


# --------------------------------
# CREAR LISTA
# --------------------------------

print()
print("Crear lugares favoritos:")

print(
    integrador.integrar(
        "lugares_favoritos",
        "cordoba",
        "lista",
        "preferencia"
    )
)


print(
    "Lugares:",
    memoria.recordar(
        "lugares_favoritos"
    )
)


# --------------------------------
# AGREGAR ELEMENTO A LA LISTA
# --------------------------------

print()
print("Agregar Mendoza:")

print(
    integrador.integrar(
        "lugares_favoritos",
        "mendoza",
        "lista",
        "preferencia"
    )
)


print(
    "Lugares:",
    memoria.recordar(
        "lugares_favoritos"
    )
)


# --------------------------------
# REPETIR ELEMENTO
# --------------------------------

print()
print("Repetir Cordoba:")

print(
    integrador.integrar(
        "lugares_favoritos",
        "cordoba",
        "lista",
        "preferencia"
    )
)


print(
    "Lugares despues de repetir:",
    memoria.recordar(
        "lugares_favoritos"
    )
)


# --------------------------------
# MOSTRAR ARCHIVO FINAL
# --------------------------------

print()
print("Archivo final:")

with open(
    "data/test_memory_integrator.json",
    "r",
    encoding="utf-8"
) as archivo:

    print(
        archivo.read()
    )

# --------------------------------
# PROBAR MEMORIA ANTIGUA
# --------------------------------

print()
print("Probar compatibilidad con memoria antigua:")


# Simulamos una memoria que todavía utiliza
# el formato anterior de KUKI.
memoria.guardar(
    "comida_favorita",
    "pizza"
)


# Ahora intentamos agregar otro valor
# utilizando el nuevo MemoryIntegrator.
print(
    integrador.integrar(
        "comida_favorita",
        "hamburguesa",
        "lista",
        "preferencia"
    )
)


# Comprobamos que la memoria antigua
# haya sido convertida automáticamente
# al nuevo formato.
print(
    "Comida favorita:",
    memoria.recordar(
        "comida_favorita"
    )
)
