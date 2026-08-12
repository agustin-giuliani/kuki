from brain.memory import Memory


memoria = Memory()

print("--- MEMORIA DE KUKI ---")

# Guardamos un recuerdo
memoria.guardar("nombre", "Agustin")

print("Recuerdo guardado.")

# Recuperamos el recuerdo
nombre = memoria.recordar("nombre")

print("KUKI recuerda:", nombre)
