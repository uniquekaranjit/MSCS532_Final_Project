# =======================================================
# Analyze HPC with comparing performance between linked list and NumPy array operations.
# Author: Unique Karanjit
# Date: Feb 23, 2025
# =======================================================

"""
Main script for comparing performance between linked list and NumPy array operations.

This script demonstrates the performance differences between linked list
and NumPy array implementations for basic traversal and sum operations.
"""

from data_structures.linked_list import create_linked_list, traverse_and_sum_linked_list
from data_structures.array_ops import create_array, traverse_and_sum_array
from performance.benchmarks import measure_execution_time, create_comparison_graph

def main():
    # Configuration
    SIZE = 1_000_000

    try:
        # Create data structures
        linked_list = create_linked_list(SIZE)
        numpy_array = create_array(SIZE)

        # Benchmark linked list
        ll_result = measure_execution_time(traverse_and_sum_linked_list, linked_list)
        
        # Benchmark NumPy array
        np_result = measure_execution_time(traverse_and_sum_array, numpy_array)

        # Print results
        print(f"Data size: {SIZE:,} elements")
        print("\nResults:")
        print(f"{'='*50}")
        print(f"Linked List:")
        print(f"  Time: {ll_result.execution_time:.6f} seconds")
        print(f"  Sum:  {ll_result.result:,}")
        print(f"\nNumPy Array:")
        print(f"  Time: {np_result.execution_time:.6f} seconds")
        print(f"  Sum:  {np_result.result:,}")
        
        # Create visualization
        create_comparison_graph(
            ll_result.execution_time,
            np_result.execution_time,
            SIZE
        )

        print("Comparision result saved as results/performance_comparision.png")
        
        # Verify results match
        assert ll_result.result == np_result.result, "Results don't match!"

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()