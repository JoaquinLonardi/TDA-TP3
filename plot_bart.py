import matplotlib.pyplot as plt
import numpy as np
from algoritmo import leer_archivo, algoritmo_iterativo
import time

def run_algorithm(input_file):
    cant_dias, ganancias, energias = leer_archivo(input_file)
    start_time = time.time()
    algoritmo_iterativo(cant_dias, ganancias, energias)
    end_time = time.time()
    run_time = end_time - start_time
    return cant_dias, run_time

# Create and run the algorithm on each test file, measuring run time
run_times_chico = []
run_times_medio = []
run_times_grande = []
sizes = []
for i in range(1, 4):
    file_name = f"test_{i}_chico.txt"
    size, run_time = run_algorithm(file_name)
    print(f"Archivo número {i}: {run_time}")
    sizes.append(size)
    run_times_chico.append(run_time)

for i in range(1, 4):
    file_name = f"test_{i}_medio.txt"
    size, run_time = run_algorithm(file_name)
    print(f"Archivo número {i}: {run_time}")
    sizes.append(size)
    run_times_medio.append(run_time)

for i in range(1, 4):
    file_name = f"test_{i}_grande.txt"
    size, run_time = run_algorithm(file_name)
    print(f"Archivo número {i}: {run_time}")
    sizes.append(size)
    run_times_grande.append(run_time)

# Sample data
categories = ['1-10', '500-1000', '10000-100000']
values1 = [10, 15, 20]
values2 = [5, 8, 12]
values3 = [7, 11, 14]

values1 = [run_times_chico[0], run_times_medio[0], run_times_grande[0]]
values2 = [run_times_chico[1], run_times_medio[1], run_times_grande[1]]
values3 = [run_times_chico[2], run_times_medio[2], run_times_grande[2]]
# Define the width of the bars
bar_width = 0.2

# Define the positions of the bars
x = np.arange(len(categories))

# Create a bar chart for each set of values
plt.bar(x - bar_width, values1, width=bar_width, label='5000 elementos', color='#FF5A5F')
plt.bar(x, values2, width=bar_width, label='7500 elementos', color='#254E70')
plt.bar(x + bar_width, values3, width=bar_width, label='10000 elementos', color='#66C3FF')

# Customize the x-axis labels
plt.xticks(x, categories)

# Add labels and a title
plt.xlabel('Rango de valores de ganancia y esfuerzo')
plt.ylabel('Tiempo de ejecución (s)')
# plt.title('Bar Chart with 3 Categories and 3 Value Sets')

# Add a legend
plt.legend()

# Show the plot
plt.show()
