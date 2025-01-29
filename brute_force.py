import sys
from itertools import combinations
import math
from a1_utils import read_input_from_cli, distance, write_output_to_file, generate_random_input_file


def brute_force_closest_pair(points: list[tuple[float, float]]) -> tuple[float, list[tuple[tuple[float, float], tuple[float, float]]]]:
    min_dist = float('inf')
    closest_pairs = set()  

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1, p2 = points[i], points[j]
            dist = distance(p1, p2)
            if dist < min_dist:
                min_dist = dist
                closest_pairs = {tuple(sorted((p1, p2)))}
            elif math.isclose(dist, min_dist):
                closest_pairs.add(tuple(sorted((p1, p2))))

    return min_dist, list(closest_pairs)


if __name__ == "__main__":
    try:
        generate_random_input_file(50000,'bf.txt')
        points = read_input_from_cli()
        min_dist, closest_pairs = brute_force_closest_pair(points)

        print(f"Minimum Distance: {min_dist}")
        print("Closest Pairs:")
        for pair in closest_pairs:
            print(pair)
        write_output_to_file(distance=min_dist, points=closest_pairs, output_file= 'brute_force_output.txt')
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
