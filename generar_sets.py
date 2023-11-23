import random

def generate_sets(num_sets, range_start, range_end, file_path):
    with open(file_path, 'w') as file:
        for _ in range(num_sets):
            # Generate a set of random numbers
            num_set = random.sample(range(range_start, range_end + 1), random.randint(2, 7))

            # Convert the set to a string and write to the file
            line = ','.join(map(str, num_set))
            file.write(line + '\n')


# Example usage:
sizes = [5, 7, 10, 15, 25, 40, 50, 75,90, 100]
for size in sizes:
    import os
    filename = f"set{size}.txt"
    path = os.path.join("sets_universo_chico", filename)
    generate_sets(size, 1, 7, path)
