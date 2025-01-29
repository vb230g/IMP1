import sys
from itertools import combinations
import math
from a1_utils import read_input_from_cli, distance, write_output_to_file

def divide_and_conquer_closest_pair(points: list[tuple[float, float]]) -> tuple[float, list[tuple[tuple[float, float], tuple[float, float]]]]:
    x_sort = sorted(points, key=lambda p: p[0])
    def closest_pair(x_sort):
        if len(x_sort) <= 3:
            min_dist = float('inf')
            closest_pairs = set()
            for i in range(len(x_sort)):
                for j in range(i + 1, len(x_sort)):
                    p1, p2 = x_sort[i], x_sort[j]
                    dist = distance(p1, p2)
                    if dist < min_dist:
                        min_dist = dist
                        closest_pairs = {tuple(sorted((p1, p2)))}
                    elif math.isclose(dist, min_dist):
                        closest_pairs.add(tuple(sorted((p1, p2))))
            return min_dist, closest_pairs  

        median_idx = len(x_sort) // 2
        median = x_sort[median_idx][0]

        left_x = x_sort[:median_idx]
        right_x = x_sort[median_idx:]

        left_dist, left_pairs = closest_pair(left_x)
        right_dist, right_pairs = closest_pair(right_x)

        if left_dist < right_dist:
            delta = left_dist
            best_pairs = left_pairs
        elif right_dist < left_dist:
            delta = right_dist
            best_pairs = right_pairs
        else:
            delta = left_dist
            best_pairs = left_pairs.union(right_pairs)  

         
        strip = [p for p in x_sort if median - delta <= p[0] <= median + delta]
        strip = sorted(strip, key=lambda p: p[1])

        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                p, q = strip[i], strip[j]
                dist = distance(p, q)
                if dist < delta:
                    delta = dist
                    best_pairs = {tuple(sorted((p, q)))}
                elif math.isclose(dist, delta):
                    best_pairs.add(tuple(sorted((p, q))))

        return delta, best_pairs
    delta, pairs = closest_pair(x_sort)
    return delta, list(pairs)
  
if __name__ == "__main__":
    try:
        points = read_input_from_cli()
        min_dist, closest_pairs = divide_and_conquer_closest_pair(points)

        print(f"Minimum Distance: {min_dist}")
        print("Closest Pairs:")
        for pair in closest_pairs:
            print(pair)
        write_output_to_file(distance=min_dist, points=closest_pairs, output_file='ddnc_output.txt')
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

