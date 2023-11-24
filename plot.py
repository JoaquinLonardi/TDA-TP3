
import os
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from algoritmo import leer_archivo
from programacion_lineal import hitting_set
from scipy.optimize import curve_fit

NUM_FILES = 20
# Function to simulate your algorithm (replace with your actual algorithm)
def run_algorithm(input_file):
    conjuntos = leer_archivo(input_file)
    conjunto_universo = set()
    for conjunto in conjuntos:
        conjunto_universo.update(conjunto)
    start_time = time.time()
    size = hitting_set(conjuntos, conjunto_universo)
    end_time = time.time()
    run_time = end_time - start_time
    return size, run_time

# Create and run the algorithm on each test file, measuring run time
files = [5, 7, 10, 15, 25, 40, 50, 75,90, 100]
run_times = []
sizes = []
for i in range(0, len(files)):
    file_name = f"set{files[i]}.txt"
    size, run_time = run_algorithm(f"sets_universo_chico/{file_name}")
    print(f"Archivo número {files[i]}: {run_time}")
    sizes.append(size)
    run_times.append(run_time)

with open("mediciones/mediciones_pl_universo_chico.txt", mode="w") as file:
    for i in range(0, len(files)):
        file.write(str(files[i]))
        file.write(',')
        file.write(str(sizes[i]))
        file.write(',')
        file.write(str(run_times[i]))


        file.write('\n')

# Create y data for the plot (run time)
plt.figure(figsize=(8, 6))
plt.xlabel('Cantidad de días')
plt.ylabel('Tiempo de ejecución (s)')
plt.scatter(sizes, run_times, label='algoritmo', marker='o', color='blue')
lines, labels = plt.gca().get_legend_handles_labels()
# ax1 = plt.twinx()
# ax1.plot(sizes, run_times, 'bo', label='algoritmo')
# Create a normalized x^2 function
# x = np.array(sizes)
x = np.linspace(min(sizes), max(sizes), 100)
y_x_squared = x ** 2
y_x_squared_normalized = y_x_squared / max(y_x_squared) * max(run_times)

# Plot x^2 with a different y-axis
ax2 = plt.twinx()
ax2.plot(x, y_x_squared_normalized, 'r-', label='x^2')

# Create x function
y_x = x  # Example of a linear function (you can replace it with any function)

# Plot x function with a different y-axis
ax3 = plt.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(x, y_x, 'g-', label='x')

# Create log(x) function
y_log_x = np.log(x)

# Plot log(x) function on a secondary y-axis
ax4 = plt.twinx()
ax4.plot(x, y_log_x, 'c-', label='log(x)')

# Create x * log(x) function
y_x_log_x = x * np.log(x)

# Plot x * log(x) function on a secondary y-axis
ax5 = plt.twinx()
# ax5.spines['right'].set_position(('outward', 60))
ax5.plot(x, y_x_log_x, 'm-', label='x * log(x)')


# ax1.get_yaxis().set_ticks([])
ax2.get_yaxis().set_ticks([])
ax3.get_yaxis().set_ticks([])
ax4.get_yaxis().set_ticks([])
ax5.get_yaxis().set_ticks([])

# Add legends
# lines, labels = plt.gca().get_legend_handles_labels()
# lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
lines4, labels4 = ax4.get_legend_handles_labels()
lines5, labels5 = ax5.get_legend_handles_labels()
plt.legend(lines + lines2 + lines3 + lines4 + lines5,
            labels + labels2 + labels3 + labels4 + labels5,
           loc='lower right')


# ax2.set_xlabel("Cantidad de días", fontsize=12)


plt.title('Tiempo de ejecución vs Días')

# Show the plot
plt.show()
