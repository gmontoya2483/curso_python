# list slicing
"""
Es una forma de Construir una nueva lista 
[x:y] x es el indice de inicio e y es el indice final,  python el indice final no se muestra
"""

# Ejemplos
friends = ['rolf', 'jose','anna', 'charlie', 'mary']
print (friends[2:4])

# Numeros negativos, comienza a contar desde el final
print (friends[-1])

# Rangos negativos
print (friends[-3:-1])

# Los tres últimos de la lista
print (friends[-3:])

# Los dos primeros de la lista
print (friends[:2])

# Desde el principio al menos 2 sin incluirlo
print (friends[:-2])

# Devuelve una lista vacia
print (friends[1:1])






