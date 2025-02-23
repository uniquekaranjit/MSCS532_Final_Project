"""
Module for performance benchmarking utilities.

This module provides functions to measure and compare
performance of different data structures and algorithms.
"""

import time
import matplotlib.pyplot as plt
import os
from typing import Callable, Any, Tuple
from dataclasses import dataclass

@dataclass
class BenchmarkResult:
    """Class to hold benchmark results."""
    execution_time: float
    result: Any

def measure_execution_time(func: Callable, *args) -> BenchmarkResult:
    """
    Measure execution time of a function.

    Args:
        func (Callable): Function to measure.
        *args: Arguments to pass to the function.

    Returns:
        BenchmarkResult: Execution time and function result.
    """
    start = time.time()
    result = func(*args)
    execution_time = time.time() - start
    return BenchmarkResult(execution_time, result)

def create_comparison_graph(ll_time: float, np_time: float, size: int) -> None:
    """
    Create and save a bar graph comparing linked list and numpy array performance.

    Args:
        ll_time (float): Execution time for linked list
        np_time (float): Execution time for numpy array
        size (int): Size of data structure used
    """
    # Create results directory if it doesn't exist
    results_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'results')
    os.makedirs(results_dir, exist_ok=True)
    
    implementations = ['Linked List', 'NumPy Array']
    times = [ll_time, np_time]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(implementations, times)
    
    # Customize the graph
    plt.title(f'Performance Comparison (n={size:,} elements)')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.6f}s',
                ha='center', va='bottom')
    
    # Save the graph in the results directory
    output_path = os.path.join(results_dir, 'performance_comparison.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close() 