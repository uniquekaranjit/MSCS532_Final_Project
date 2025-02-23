# MSCS532_Final_Project

# Data Structure Performance Comparison

## Overview
This project demonstrates and analyzes the performance differences between linked lists and NumPy arrays in Python, specifically focusing on traversal and summation operations. 
## Project Structure
```
project/
├── data_structures/
│   ├── __init__.py
│   ├── linked_list.py    # Linked list implementation
│   └── array_ops.py      # NumPy array operations
├── performance/
│   ├── __init__.py
│   └── benchmarks.py     # Benchmarking utilities
├── main.py               # Main execution script
└── README.md
```

## Features
- Implementation of singly linked list
- Optimized NumPy array operations
- Comprehensive benchmarking suite

## Requirements
- Python 3.7+
- NumPy
- Matplotlib

## Dependencies

1. Install dependencies:
```bash
pip install numpy matplotlib
```

## Usage
Run the main script to execute the performance comparison:
```bash
python main.py
```

The script will:
1. Create both data structures with 1 million elements
2. Measure traversal and sum operation performance
3. Display detailed timing results
4. Generate and save a performance comparison graph in `results/performance_comparison.png`
5. Verify correctness of results

## Sample Output
```
Data size: 1,000,000 elements

Results:
==================================================
Linked List:
  Time: 0.123456 seconds
  Sum:  499999500000

NumPy Array:
  Time: 0.001234 seconds
  Sum:  499999500000
```

A bar graph comparing the performance will be saved in the `results` directory.

