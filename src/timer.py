"""
Timer Module for Algorithm Analysis - Activity 06
CS101 Fall 2025 - Build a Better Algorithm

This module provides timing and analysis tools for the four algorithms.
Students will use these functions to measure and understand algorithm complexity.
"""

import time

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

from algorithms import (
    array_access, binary_search_iterative, linear_search_with_counter,
    find_all_pairs_with_sum, generate_test_data, generate_sorted_test_data
)


def run_algorithm_experiment(algorithm_name, input_sizes):
    """
    Run timing experiments on a specific algorithm with different input sizes.
    
    Args:
        algorithm_name (str): Name of algorithm to test
        input_sizes (list): List of input sizes to test
        
    Returns:
        dict: Results including times, ratios, and analysis
    """
    print(f"\n{'='*50}")
    print(f"TESTING: {algorithm_name.upper()}")
    print(f"{'='*50}")
    
    results = {
        'algorithm': algorithm_name,
        'sizes': input_sizes,
        'times': [],
        'ratios': [],
        'operations': [],  # For algorithms that count operations
        'description': get_algorithm_description(algorithm_name)
    }
    
    for i, size in enumerate(input_sizes):
        print(f"Running with input size: {size}...")
        
        # Run the specific algorithm
        execution_time, operation_count = run_single_algorithm(algorithm_name, size)
        
        results['times'].append(execution_time)
        results['operations'].append(operation_count)
        
        # Calculate ratio compared to previous size
        if i > 0:
            ratio = execution_time / results['times'][i-1] if results['times'][i-1] > 0 else 1.0
            results['ratios'].append(ratio)
        else:
            results['ratios'].append(0)  # No ratio for first measurement
    
    return results


def run_single_algorithm(algorithm_name, size):
    """
    Run a single algorithm with the given input size.
    
    Args:
        algorithm_name (str): Name of algorithm to run
        size (int): Size of input data
        
    Returns:
        tuple: (execution_time, operation_count)
    """
    trials = 3  # Run multiple times for better accuracy
    times = []
    operation_counts = []
    
    for _ in range(trials):
        if algorithm_name == "Array Access":
            # Test array access with random indices
            data = generate_test_data(size)
            indices_to_test = [size // 4, size // 2, size * 3 // 4]  # Test a few positions
            
            start_time = time.time()
            for index in indices_to_test:
                array_access(data, index)
            end_time = time.time()
            
            times.append(end_time - start_time)
            operation_counts.append(len(indices_to_test))  # Number of accesses
            
        elif algorithm_name == "Binary Search":
            # Test binary search on sorted data
            data = generate_sorted_test_data(size)
            target = data[size * 3 // 4] if size > 0 else 1  # Search for element that exists
            
            start_time = time.time()
            result = binary_search_iterative(data, target)
            end_time = time.time()
            
            times.append(end_time - start_time)
            # Estimate operations: log₂(size) comparisons
            import math
            operation_counts.append(math.ceil(math.log2(size)) if size > 0 else 1)
            
        elif algorithm_name == "Linear Search":
            # Test linear search (worst case - search for last element)
            data = generate_test_data(size)
            target = data[-1] if size > 0 else 1  # Last element (worst case)
            
            start_time = time.time()
            result_index, comparisons = linear_search_with_counter(data, target)
            end_time = time.time()
            
            times.append(end_time - start_time)
            operation_counts.append(comparisons)
            
        elif algorithm_name == "Find All Pairs":
            # Test pair finding (use smaller size to avoid long execution)
            actual_size = min(size, 200)  # Cap at 200 to keep reasonable timing
            data = generate_test_data(actual_size)
            target_sum = data[0] + data[1] if actual_size >= 2 else 10
            
            start_time = time.time()
            pairs, comparisons = find_all_pairs_with_sum(data, target_sum)
            end_time = time.time()
            
            times.append(end_time - start_time)
            operation_counts.append(comparisons)
    
    # Return average time and typical operation count
    avg_time = sum(times) / len(times)
    typical_operations = operation_counts[0]  # They should all be similar
    
    return avg_time, typical_operations


def get_algorithm_description(algorithm_name):
    """Get a description of the algorithm's expected complexity."""
    descriptions = {
        "Array Access": {
            "complexity": "O(1) - Constant Time",
            "explanation": "Direct memory access - same time regardless of array size",
            "pattern": "Time should stay roughly constant as input size increases"
        },
        "Binary Search": {
            "complexity": "O(log n) - Logarithmic Time", 
            "explanation": "Eliminates half the search space each step",
            "pattern": "Time should grow very slowly - doubling input adds only one step"
        },
        "Linear Search": {
            "complexity": "O(n) - Linear Time",
            "explanation": "Must potentially check every element in worst case",
            "pattern": "Time should double when input size doubles"
        },
        "Find All Pairs": {
            "complexity": "O(n²) - Quadratic Time",
            "explanation": "Nested loops check every pair of elements",
            "pattern": "Time should quadruple when input size doubles"
        }
    }
    return descriptions.get(algorithm_name, {"complexity": "Unknown", "explanation": "", "pattern": ""})


def print_algorithm_results(results):
    """
    Print formatted results for an algorithm experiment.
    
    Args:
        results (dict): Results from run_algorithm_experiment
    """
    algorithm = results['algorithm']
    sizes = results['sizes']
    times = results['times']
    ratios = results['ratios']
    operations = results['operations']
    desc = results['description']
    
    print(f"\n=== {algorithm.upper()} RESULTS ===")
    print(f"Expected Complexity: {desc['complexity']}")
    print(f"Why: {desc['explanation']}")
    print(f"Pattern to Watch: {desc['pattern']}\n")
    
    # Print results table
    print(f"{'Size':>8} | {'Time (sec)':>12} | {'Ratio':>8} | {'Operations':>12}")
    print("-" * 50)
    
    for i, size in enumerate(sizes):
        time_str = f"{times[i]:.6f}"
        ratio_str = "─" if i == 0 else f"{ratios[i]:.2f}"
        ops_str = f"{operations[i]}"
        
        print(f"{size:>8} | {time_str:>12} | {ratio_str:>8} | {ops_str:>12}")
    
    # Analyze the pattern
    print(f"\n--- ANALYSIS ---")
    if len(ratios) > 1:
        avg_ratio = sum(ratios[1:]) / len(ratios[1:])  # Skip first ratio (which is 0)
        print(f"Average ratio between consecutive sizes: {avg_ratio:.2f}")
        
        if algorithm == "Array Access":
            if avg_ratio < 1.5:
                print("✓ GOOD: Ratios close to 1.0 confirm constant time O(1)")
            else:
                print("? UNEXPECTED: Ratios should be close to 1.0 for O(1)")
                
        elif algorithm == "Binary Search":
            if 1.0 <= avg_ratio <= 1.5:
                print("✓ GOOD: Small ratios confirm logarithmic time O(log n)")
            else:
                print("? UNEXPECTED: Ratios should be small (1.0-1.5) for O(log n)")
                
        elif algorithm == "Linear Search":
            if 1.8 <= avg_ratio <= 2.2:
                print("✓ GOOD: Ratios close to 2.0 confirm linear time O(n)")
            else:
                print("? UNEXPECTED: Ratios should be close to 2.0 for O(n)")
                
        elif algorithm == "Find All Pairs":
            if 3.5 <= avg_ratio <= 4.5:
                print("✓ GOOD: Ratios close to 4.0 confirm quadratic time O(n²)")
            else:
                print("? UNEXPECTED: Ratios should be close to 4.0 for O(n²)")
    
    print()


def create_comparison_plot(results_list):
    """
    Create a plot comparing multiple algorithms.
    
    Args:
        results_list (list): List of results from different algorithms
    """
    if not MATPLOTLIB_AVAILABLE:
        print("⚠️  Matplotlib not available. Creating text visualization instead...")
        create_text_visualization(results_list)
        return
        
    try:
        plt.figure(figsize=(12, 8))
        
        for results in results_list:
            plt.plot(results['sizes'], results['times'], 
                    marker='o', linewidth=2, markersize=8, 
                    label=f"{results['algorithm']} - {results['description']['complexity']}")
        
        plt.xlabel("Input Size")
        plt.ylabel("Execution Time (seconds)")
        plt.title("Algorithm Performance Comparison")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Use log scale if there are big differences
        max_time = max(max(r['times']) for r in results_list)
        min_time = min(min(r['times']) for r in results_list if min(r['times']) > 0)
        
        if max_time / min_time > 100:  # If more than 100x difference
            plt.yscale('log')
            plt.ylabel("Execution Time (seconds) - Log Scale")
        
        plt.tight_layout()
        plt.savefig('algorithm_comparison.png', dpi=150, bbox_inches='tight')
        plt.show()
        
        print("📊 Performance comparison plot saved as 'algorithm_comparison.png'")
        
    except ImportError:
        print("⚠️  Matplotlib not available. Install with: uv add matplotlib")
        create_text_visualization(results_list)


def create_text_visualization(results_list):
    """
    Create a simple text-based visualization when matplotlib isn't available.
    
    Args:
        results_list (list): List of results from different algorithms
    """
    print("\n" + "="*60)
    print("TEXT-BASED PERFORMANCE VISUALIZATION")
    print("="*60)
    
    for results in results_list:
        algorithm = results['algorithm']
        times = results['times']
        sizes = results['sizes']
        
        print(f"\n{algorithm} - {results['description']['complexity']}")
        print("-" * 40)
        
        # Normalize times for visualization (scale to 50 characters max)
        max_time = max(times) if times else 1
        
        for i, (size, time_val) in enumerate(zip(sizes, times)):
            bar_length = int((time_val / max_time) * 50)
            bar = "█" * bar_length
            print(f"{size:>6}: {bar} ({time_val:.6f}s)")


def save_results_to_file(results_list, filename="algorithm_analysis_results.txt"):
    """
    Save experiment results to a text file.
    
    Args:
        results_list (list): List of algorithm results
        filename (str): Name of output file
    """
    with open(filename, 'w') as f:
        f.write("ALGORITHM ANALYSIS RESULTS - Activity 06\n")
        f.write("CS101 Fall 2025 - Build a Better Algorithm\n")
        f.write("="*60 + "\n\n")
        
        for results in results_list:
            algorithm = results['algorithm']
            sizes = results['sizes']
            times = results['times']
            ratios = results['ratios']
            operations = results['operations']
            desc = results['description']
            
            f.write(f"ALGORITHM: {algorithm}\n")
            f.write(f"Complexity: {desc['complexity']}\n")
            f.write(f"Explanation: {desc['explanation']}\n\n")
            
            f.write(f"{'Size':>8} | {'Time (sec)':>12} | {'Ratio':>8} | {'Operations':>12}\n")
            f.write("-" * 50 + "\n")
            
            for i, size in enumerate(sizes):
                time_str = f"{times[i]:.6f}"
                ratio_str = "─" if i == 0 else f"{ratios[i]:.2f}"
                ops_str = f"{operations[i]}"
                
                f.write(f"{size:>8} | {time_str:>12} | {ratio_str:>8} | {ops_str:>12}\n")
            
            f.write("\n" + "-"*50 + "\n\n")
    
    print(f"📁 Results saved to '{filename}'")


def get_input_sizes():
    """
    Get input sizes for the experiment from the user.
    
    Returns:
        list: List of input sizes to test
    """
    print("Choose experiment sizes for testing your algorithm:")
    print("1. Small test: 100, 200, 400, 800")
    print("2. Medium test: 500, 1000, 2000, 4000") 
    print("3. Large test: 1000, 2000, 4000, 8000")
    print("4. Custom sizes")
    
    while True:
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            return [100, 200, 400, 800]
        elif choice == "2":
            return [500, 1000, 2000, 4000]
        elif choice == "3":
            return [1000, 2000, 4000, 8000]
        elif choice == "4":
            return get_custom_sizes()
        else:
            print("Please enter 1, 2, 3, or 4")


def get_custom_sizes():
    """Get custom input sizes from user."""
    print("\nEnter custom sizes separated by commas (e.g., 100,200,400,800)")
    print("Recommended: Use at least 4 sizes, keep them reasonable (50-10000)")
    
    while True:
        try:
            sizes_input = input("Enter sizes: ").strip()
            sizes = [int(s.strip()) for s in sizes_input.split(',')]
            
            if len(sizes) < 3:
                print("Please enter at least 3 sizes for meaningful analysis")
                continue
            if any(s < 10 or s > 50000 for s in sizes):
                print("Please keep sizes between 10 and 50000")
                continue
                
            sizes.sort()
            print(f"Using sizes: {sizes}")
            return sizes
            
        except ValueError:
            print("Please enter valid numbers separated by commas")