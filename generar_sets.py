import random
import numpy as np

def generate_sets(num_sets, inicio_universo, fin_universo, file_path, b):
    with open(file_path, 'w') as file:
        for _ in range(num_sets):

            cardinalidad_conjunto_actual = random.randint(2, b)
            # Generate a set of random numbers
            # print(f"Inicio: {inicio_universo}. Fin {fin_universo + 1}. Cardinalidad: {cardinalidad_conjunto_actual}")
            num_set = random.sample(range(inicio_universo, fin_universo + 1), cardinalidad_conjunto_actual)

            # Convert the set to a string and write to the file
            line = ','.join(map(str, num_set))
            file.write(line + '\n')


# Example usage:
# sizes = [100, 150, 200, 300, 500, 750, 1000]
# sizes = [10,20,30,40,50,60,70,80,90,100,200,500]
# n = []
sizes = [10,20,30,40,50,60,70,80,90,100,200,500]
fin_universo = 10000
tamanos_maximos = np.linspace(2, fin_universo, len(sizes))
size_universo = np.linspace(5000, fin_universo, len(sizes), dtype=int)
np.random.shuffle(tamanos_maximos)
for i, size in enumerate(sizes):
    import os
    filename = f"set{size}.txt"
    path = os.path.join("sets_mediciones_exageradas_mas", filename)
    print(size_universo[i])
    generate_sets(size, 1, fin_universo, path, size_universo[i])
