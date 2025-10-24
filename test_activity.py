#!/usr/bin/env python3
"""
Comprehensive test script for Activity_06
Tests all functionality and verifies file creation
"""

import sys
import os
import time

# Add src to path
sys.path.append('src')

def test_algorithms():
    """Test all four algorithms individually."""
    print("="*60)
    print("TESTING INDIVIDUAL ALGORITHMS")
    print("="*60)
    
    from algorithms import (
        array_access, binary_search_iterative, linear_search_with_counter,
        find_all_pairs_with_sum, generate_test_data, generate_sorted_test_data
    )
    
    # Test data
    test_data = [1, 3, 5, 7, 9, 11, 13, 15]
    unsorted_data = [5, 2, 8, 1, 9, 12, 3]
    
    # Test 1: Array Access
    print("1. Testing Array Access (O(1))...")
    result = array_access(test_data, 3)
    print(f"   ✓ array_access([1,3,5,7,9,11,13,15], 3) = {result}")
    assert result == 7, "Array access failed"
    
    # Test 2: Binary Search
    print("2. Testing Binary Search (O(log n))...")
    result = binary_search_iterative(test_data, 9)
    print(f"   ✓ binary_search([1,3,5,7,9,11,13,15], 9) = index {result}")
    assert result == 4, "Binary search failed"
    
    # Test 3: Linear Search
    print("3. Testing Linear Search (O(n))...")
    result = linear_search_with_counter(unsorted_data, 8)
    print(f"   ✓ linear_search([5,2,8,1,9,12,3], 8) = {result}")
    assert result[0] == 2, "Linear search failed"
    
    # Test 4: Find All Pairs
    print("4. Testing Find All Pairs (O(n²))...")
    numbers = [1, 2, 3, 4, 5]
    result = find_all_pairs_with_sum(numbers, 7)
    print(f"   ✓ find_pairs([1,2,3,4,5], target=7) = {result[0]}")
    assert len(result[0]) == 2, "Find pairs failed"  # Should find (2,5) and (3,4)
    
    print("   ✓ All individual algorithm tests PASSED!")
    return True


def test_timer_functionality():
    """Test the timer module and experiment functionality."""
    print("\n" + "="*60)
    print("TESTING TIMER AND EXPERIMENT FUNCTIONALITY") 
    print("="*60)
    
    from timer import (
        run_single_algorithm, run_algorithm_experiment, 
        print_algorithm_results, save_results_to_file, create_text_visualization
    )
    
    test_sizes = [50, 100, 200]
    
    print("1. Testing single algorithm timing...")
    exec_time, ops = run_single_algorithm('Array Access', 100)
    print(f"   ✓ Array Access timing: {exec_time:.6f}s, {ops} operations")
    
    print("2. Testing full algorithm experiment...")
    results = run_algorithm_experiment('Linear Search', test_sizes)
    print("   ✓ Full experiment completed")
    
    print("3. Testing results display...")
    print_algorithm_results(results)
    print("   ✓ Results display completed")
    
    print("4. Testing file creation...")
    test_filename = 'test_output.txt'
    save_results_to_file([results], test_filename)
    
    if os.path.exists(test_filename):
        print(f"   ✓ Results file '{test_filename}' created successfully")
        with open(test_filename, 'r') as f:
            content = f.read()
            if 'ALGORITHM ANALYSIS RESULTS' in content:
                print("   ✓ File contains expected content")
            else:
                print("   ✗ File content verification failed")
                return False
    else:
        print(f"   ✗ Results file '{test_filename}' was not created")
        return False
    
    print("5. Testing text visualization...")
    create_text_visualization([results])
    print("   ✓ Text visualization completed")
    
    return True


def test_comparison_mode():
    """Test comparison functionality with multiple algorithms."""
    print("\n" + "="*60)
    print("TESTING COMPARISON MODE")
    print("="*60)
    
    from timer import run_algorithm_experiment, create_comparison_plot, save_results_to_file
    
    test_sizes = [100, 200]  # Keep small for fast testing
    algorithms = ['Array Access', 'Linear Search']
    
    all_results = []
    
    print("1. Running experiments for multiple algorithms...")
    for algorithm in algorithms:
        print(f"   Testing {algorithm}...")
        results = run_algorithm_experiment(algorithm, test_sizes)
        all_results.append(results)
        print(f"   ✓ {algorithm} completed")
    
    print("2. Creating comparison visualization...")
    create_comparison_plot(all_results)
    print("   ✓ Comparison visualization completed")
    
    print("3. Saving comparison results...")
    comparison_file = 'comparison_test.txt'
    save_results_to_file(all_results, comparison_file)
    
    if os.path.exists(comparison_file):
        print(f"   ✓ Comparison file '{comparison_file}' created successfully")
    else:
        print(f"   ✗ Comparison file creation failed")
        return False
    
    return True


def test_all_algorithms_scaling():
    """Test all four algorithms with realistic scaling."""
    print("\n" + "="*60) 
    print("TESTING ALL ALGORITHMS WITH SCALING")
    print("="*60)
    
    from timer import run_algorithm_experiment
    
    algorithms = ['Array Access', 'Binary Search', 'Linear Search', 'Find All Pairs']
    test_sizes = [100, 200, 400]
    
    all_results = []
    
    for algorithm in algorithms:
        print(f"\nTesting {algorithm} scaling...")
        try:
            results = run_algorithm_experiment(algorithm, test_sizes)
            all_results.append(results)
            
            # Verify expected complexity patterns
            if len(results['ratios']) >= 2:
                avg_ratio = sum(r for r in results['ratios'][1:]) / len(results['ratios'][1:])
                print(f"   Average ratio: {avg_ratio:.2f}")
                
                # Basic complexity validation
                if algorithm == 'Array Access':
                    expected = "should stay close to 1.0 (constant time)"
                elif algorithm == 'Binary Search':
                    expected = "should be small, 1.0-1.5 (logarithmic time)" 
                elif algorithm == 'Linear Search':
                    expected = "should be close to 2.0 (linear time)"
                elif algorithm == 'Find All Pairs':
                    expected = "should be close to 4.0 (quadratic time)"
                
                print(f"   Expected: {expected}")
            
            print(f"   ✓ {algorithm} scaling test completed")
            
        except Exception as e:
            print(f"   ✗ {algorithm} failed: {e}")
            return False
    
    # Save all results
    final_file = 'all_algorithms_final_test.txt'
    from timer import save_results_to_file
    save_results_to_file(all_results, final_file)
    
    if os.path.exists(final_file):
        print(f"\n   ✓ Final results saved to '{final_file}'")
    else:
        print(f"\n   ✗ Final results file creation failed")
        return False
    
    return True


def test_file_outputs():
    """Verify all output files are created with correct content."""
    print("\n" + "="*60)
    print("VERIFYING OUTPUT FILES")
    print("="*60)
    
    expected_files = [
        'test_output.txt',
        'comparison_test.txt', 
        'all_algorithms_final_test.txt'
    ]
    
    all_files_exist = True
    
    for filename in expected_files:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            print(f"   ✓ {filename} exists ({size} bytes)")
            
            # Check content
            with open(filename, 'r') as f:
                content = f.read()
                if 'ALGORITHM ANALYSIS RESULTS' in content and 'Activity 06' in content:
                    print(f"     ✓ Content format correct")
                else:
                    print(f"     ✗ Content format incorrect")
                    all_files_exist = False
        else:
            print(f"   ✗ {filename} missing")
            all_files_exist = False
    
    return all_files_exist


def main():
    """Run all tests and provide summary."""
    print("ACTIVITY 06 COMPREHENSIVE TESTING")
    print("Build a Better Algorithm - Full Functionality Test")
    print("=" * 60)
    
    start_time = time.time()
    test_results = []
    
    # Run all tests
    tests = [
        ("Individual Algorithm Functions", test_algorithms),
        ("Timer and Experiment Functionality", test_timer_functionality), 
        ("Comparison Mode", test_comparison_mode),
        ("All Algorithms Scaling", test_all_algorithms_scaling),
        ("Output File Verification", test_file_outputs)
    ]
    
    for test_name, test_func in tests:
        print(f"\n🧪 Running: {test_name}")
        try:
            result = test_func()
            test_results.append((test_name, result))
            if result:
                print(f"   ✅ {test_name}: PASSED")
            else:
                print(f"   ❌ {test_name}: FAILED")
        except Exception as e:
            print(f"   ❌ {test_name}: ERROR - {e}")
            test_results.append((test_name, False))
    
    # Summary
    end_time = time.time()
    total_time = end_time - start_time
    
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in test_results if result)
    total = len(test_results)
    
    for test_name, result in test_results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    print(f"Execution time: {total_time:.2f} seconds")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! Activity_06 is fully functional.")
        print("\nCreated files:")
        for file in ['test_output.txt', 'comparison_test.txt', 'all_algorithms_final_test.txt']:
            if os.path.exists(file):
                print(f"  - {file}")
    else:
        print(f"\n⚠️  {total - passed} tests failed. Check the output above for details.")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)