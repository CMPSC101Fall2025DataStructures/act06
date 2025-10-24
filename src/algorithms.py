"""
Four Algorithm Examples for Complexity Analysis - Activity 06
CS101 Fall 2025 - Build a Better Algorithm

This module contains four algorithms with different time complexities that students
will analyze and discuss. Each algorithm is simple, well-commented, and demonstrates
a different Big-O complexity pattern.

The four problems and their solutions:
1. Array Access (O(1)) - Constant time
2. Binary Search (O(log n)) - Logarithmic time  
3. Linear Search (O(n)) - Linear time
4. Find All Pairs (O(n²)) - Quadratic time
"""

import random
import time


def array_access(data_list, index):
    """
    PROBLEM: Get the value at a specific position in a list.
    
    ALGORITHM: Direct array access using indexing
    TIME COMPLEXITY: O(1) - Constant time
    
    Why O(1)?
    - Arrays store elements in consecutive memory locations
    - We can calculate the exact memory address: base + (index × element_size)
    - No matter if the list has 10 elements or 10 million, accessing by index
      takes the same amount of time!
    
    Args:
        data_list (list): The list to access
        index (int): The index to retrieve (0-based)
        
    Returns:
        element: The value at the specified index
        
    Real-world example: Looking up a student's grade by their student ID number
    """
    # This is O(1) because we go directly to the memory location
    # The computer doesn't need to search through other elements
    if 0 <= index < len(data_list):
        return data_list[index]  # Direct access - always same time!
    else:
        return None  # Index out of bounds


def binary_search_iterative(sorted_list, target):
    """
    PROBLEM: Find if a number exists in a sorted list.
    
    ALGORITHM: Binary search (divide and conquer)
    TIME COMPLEXITY: O(log n) - Logarithmic time
    
    Why O(log n)?
    - Each step eliminates half of the remaining possibilities
    - If we have 1000 elements, we need at most 10 steps (2^10 = 1024)
    - If we have 1 million elements, we need at most 20 steps (2^20 ≈ 1M)
    - Doubling the input size only adds one more step!
    
    Args:
        sorted_list (list): A list sorted in ascending order
        target: The value to search for
        
    Returns:
        int: Index of target if found, -1 if not found
        
    Real-world example: Looking up a word in a dictionary by flipping to middle pages
    """
    left = 0
    right = len(sorted_list) - 1
    
    while left <= right:
        # Find the middle point
        middle = (left + right) // 2
        
        # Check if we found our target
        if sorted_list[middle] == target:
            return middle  # Found it!
        
        # If target is smaller, search the left half
        elif sorted_list[middle] > target:
            right = middle - 1  # Eliminate right half
            
        # If target is larger, search the right half  
        else:
            left = middle + 1   # Eliminate left half
    
    return -1  # Not found after eliminating all possibilities


def linear_search_with_counter(data_list, target):
    """
    PROBLEM: Find if a number exists in an unsorted list.
    
    ALGORITHM: Linear search (check each element one by one)
    TIME COMPLEXITY: O(n) - Linear time
    
    Why O(n)?
    - In the worst case, we might need to check every single element
    - If we double the list size, we potentially double the search time
    - The time grows proportionally with the input size
    
    Args:
        data_list (list): The list to search through (can be unsorted)
        target: The value to search for
        
    Returns:
        tuple: (index if found or -1, number of elements checked)
        
    Real-world example: Looking for your keys by checking every pocket one by one
    """
    comparisons = 0  # Count how many elements we check
    
    # Check each element in order
    for i in range(len(data_list)):
        comparisons += 1
        
        if data_list[i] == target:
            return (i, comparisons)  # Found it after 'comparisons' checks
    
    return (-1, comparisons)  # Not found, but checked all 'comparisons' elements


def find_all_pairs_with_sum(numbers, target_sum):
    """
    PROBLEM: Find all pairs of numbers in a list that add up to a target sum.
    
    ALGORITHM: Nested loops to check every possible pair
    TIME COMPLEXITY: O(n²) - Quadratic time
    
    Why O(n²)?
    - We use nested loops: for each element, we check it against every other element
    - If we have n elements, we make roughly n × n = n² comparisons
    - If we double the list size, we quadruple the number of operations!
    - 100 elements → ~10,000 operations
    - 200 elements → ~40,000 operations
    
    Args:
        numbers (list): List of numbers to check
        target_sum: The sum we're looking for
        
    Returns:
        tuple: (list of pairs that sum to target, number of comparisons made)
        
    Real-world example: Finding all pairs of people whose ages add up to 50
    """
    pairs = []
    comparisons = 0
    
    # Check every possible pair (i, j) where i < j
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):  # Start from i+1 to avoid duplicates
            comparisons += 1
            
            # Check if this pair sums to our target
            if numbers[i] + numbers[j] == target_sum:
                pairs.append((numbers[i], numbers[j]))
    
    return (pairs, comparisons)


# Helper functions for testing and demonstration

def generate_test_data(size, min_val=1, max_val=1000):
    """Generate random test data for the algorithms."""
    return [random.randint(min_val, max_val) for _ in range(size)]


def generate_sorted_test_data(size, min_val=1, max_val=1000):
    """Generate sorted test data for binary search."""
    data = generate_test_data(size, min_val, max_val)
    return sorted(data)


def time_algorithm_with_setup(algorithm_func, setup_func, size, *args):
    """
    Time an algorithm while excluding the setup time.
    
    Args:
        algorithm_func: The algorithm to time
        setup_func: Function to generate test data  
        size: Size of test data to generate
        *args: Additional arguments for the algorithm
        
    Returns:
        tuple: (execution_time, result, test_data_used)
    """
    # Generate test data (don't time this part)
    test_data = setup_func(size)
    
    # Time only the algorithm execution
    start_time = time.time()
    result = algorithm_func(test_data, *args)
    end_time = time.time()
    
    execution_time = end_time - start_time
    return (execution_time, result, test_data)


def demonstrate_complexity_differences():
    """
    Quick demonstration showing how each algorithm scales differently.
    This function shows the key differences students should observe.
    """
    print("=== COMPLEXITY DEMONSTRATION ===")
    print("Watch how execution time changes as input size grows...\n")
    
    sizes = [100, 200, 400, 800]
    
    for size in sizes:
        print(f"Input size: {size}")
        
        # Test array access (O(1)) - should stay constant
        data = generate_test_data(size)
        start = time.time()
        array_access(data, size // 2)  # Access middle element
        access_time = time.time() - start
        
        # Test linear search (O(n)) - should grow linearly  
        start = time.time()
        linear_search_with_counter(data, data[-1])  # Search for last element (worst case)
        linear_time = time.time() - start
        
        # Test binary search (O(log n)) - should grow slowly
        sorted_data = sorted(data)
        start = time.time()
        binary_search_iterative(sorted_data, sorted_data[-1])  # Search for last element
        binary_time = time.time() - start
        
        # Test pair finding (O(n²)) - should grow quadratically
        small_data = data[:min(50, size)]  # Keep this small to avoid long waits
        start = time.time()
        find_all_pairs_with_sum(small_data, small_data[0] + small_data[1])
        pairs_time = time.time() - start
        
        print(f"  Array access: {access_time:.6f} seconds")
        print(f"  Linear search: {linear_time:.6f} seconds") 
        print(f"  Binary search: {binary_time:.6f} seconds")
        print(f"  Find pairs: {pairs_time:.6f} seconds")
        print()


# Algorithm validation helpers

def verify_binary_search(sorted_list, target, result):
    """Verify that binary search returned the correct result."""
    if result == -1:
        return target not in sorted_list
    elif 0 <= result < len(sorted_list):
        return sorted_list[result] == target
    else:
        return False


def verify_linear_search(data_list, target, result_tuple):
    """Verify that linear search returned the correct result."""
    index, comparisons = result_tuple
    if index == -1:
        return target not in data_list and comparisons == len(data_list)
    elif 0 <= index < len(data_list):
        return data_list[index] == target and comparisons == index + 1
    else:
        return False


def verify_pairs(numbers, target_sum, result_tuple):
    """Verify that all returned pairs actually sum to the target."""
    pairs, comparisons = result_tuple
    for pair in pairs:
        if len(pair) != 2 or pair[0] + pair[1] != target_sum:
            return False
    return True