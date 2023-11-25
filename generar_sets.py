import random

def generate_sets(num_sets, range_start, range_end, file_path):
    with open(file_path, 'w') as file:
        for _ in range(num_sets):
            # Generate a set of random numbers
            num_set = random.sample(range(range_start, range_end + 1), random.randint(2, 20))

            # Convert the set to a string and write to the file
            line = ','.join(map(str, num_set))
            file.write(line + '\n')


# Example usage:
# sizes = [100, 150, 200, 300, 500, 750, 1000]
# sizes = [10,20,30,40,50,60,70,80,90,100,200,500]
# n = []
sizes = [100, 200, 300]
for size in sizes:
    import os
    filename = f"set{size}.txt"
    path = os.path.join("sets_mediciones_exageradas", filename)
    generate_sets(10, 1, size, path)
