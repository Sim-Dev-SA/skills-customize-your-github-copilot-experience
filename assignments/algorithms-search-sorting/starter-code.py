# Starter Code: Algorithmic Thinking with Search and Sorting

import random
import time


def linear_search(numbers, target):
    """Return the index of target in numbers, or -1 if not found."""
    # TODO: Implement linear search
    return -1


def binary_search(sorted_numbers, target):
    """Return the index of target in sorted_numbers, or -1 if not found."""
    # TODO: Implement binary search
    return -1


def bubble_sort(numbers):
    """Return a sorted copy of numbers in ascending order."""
    # TODO: Implement bubble sort
    return numbers


def time_search(search_function, numbers, target):
    start = time.perf_counter()
    result = search_function(numbers, target)
    duration = time.perf_counter() - start
    return result, duration


def main():
    # Small test cases for correctness
    test_numbers = [3, 9, 1, 6, 4, 8]
    target = 6

    print("Small list:", test_numbers)
    print("Target:", target)
    print("linear_search ->", linear_search(test_numbers, target))

    sorted_test_numbers = bubble_sort(test_numbers[:])
    print("Sorted list:", sorted_test_numbers)
    print("binary_search ->", binary_search(sorted_test_numbers, target))

    # Larger dataset for simple timing comparison
    large_numbers = [random.randint(1, 50_000) for _ in range(5_000)]
    large_sorted_numbers = bubble_sort(large_numbers[:])

    large_target = large_sorted_numbers[len(large_sorted_numbers) // 2]

    linear_result, linear_time = time_search(linear_search, large_numbers, large_target)
    binary_result, binary_time = time_search(binary_search, large_sorted_numbers, large_target)

    print("\nPerformance comparison (target should be found):")
    print(f"linear_search -> index={linear_result}, time={linear_time:.6f}s")
    print(f"binary_search -> index={binary_result}, time={binary_time:.6f}s")


if __name__ == "__main__":
    main()
