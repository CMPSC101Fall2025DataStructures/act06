"""
Main Program - Activity 06: Build a Better Algorithm
CS101 Fall 2025

Interactive program where students choose an algorithm to study and analyze its complexity.
This follows the "Build a Better Algorithm" approach where students explore different
algorithmic solutions and reason about their efficiency.
"""

from timer import (
    run_algorithm_experiment, print_algorithm_results, 
    create_comparison_plot, save_results_to_file, get_input_sizes
)


def display_algorithm_menu():
    """Display the menu of available algorithms for students to choose from."""
    print("\n" + "="*60)
    print("WELCOME TO 'BUILD A BETTER ALGORITHM'")
    print("="*60)
    print("In this activity, you'll explore four different algorithms that solve")
    print("different problems. Each has a different time complexity!")
    print()
    print("Available algorithms to study:")
    print()
    
    print("1. 🎯 ARRAY ACCESS - O(1) Constant Time")
    print("   Problem: Get a value at a specific position in a list")
    print("   Example: data[5] → gets the 6th element instantly")
    print("   Real-world: Looking up a student's grade by ID number")
    print()
    
    print("2. 🔍 BINARY SEARCH - O(log n) Logarithmic Time") 
    print("   Problem: Find if a number exists in a sorted list")
    print("   Example: Find 'Smith' in a sorted phone book")
    print("   Real-world: Dictionary lookup, database indexes")
    print()
    
    print("3. 🔎 LINEAR SEARCH - O(n) Linear Time")
    print("   Problem: Find if a number exists in an unsorted list")  
    print("   Example: Find your keys by checking every pocket")
    print("   Real-world: Finding a file on an unorganized computer")
    print()
    
    print("4. 👥 FIND ALL PAIRS - O(n²) Quadratic Time")
    print("   Problem: Find all pairs of numbers that sum to a target")
    print("   Example: Find all pairs of people whose ages add to 50")
    print("   Real-world: Finding compatible team members, matching algorithms")
    print()


def get_algorithm_choice():
    """
    Get the student's algorithm choice and return the algorithm name.
    
    Returns:
        str: Name of chosen algorithm
    """
    algorithms = {
        "1": "Array Access",
        "2": "Binary Search", 
        "3": "Linear Search",
        "4": "Find All Pairs"
    }
    
    while True:
        choice = input("Which algorithm would you like to study? (1-4): ").strip()
        
        if choice in algorithms:
            return algorithms[choice]
        else:
            print("Please enter 1, 2, 3, or 4")


def explain_algorithm_details(algorithm_name):
    """
    Provide detailed explanation of the chosen algorithm before running experiments.
    
    Args:
        algorithm_name (str): Name of the algorithm to explain
    """
    explanations = {
        "Array Access": {
            "problem": "Getting a value at a specific position in an array/list",
            "how_it_works": [
                "Arrays store elements in consecutive memory locations",
                "Computer calculates exact address: base_address + (index × element_size)",
                "Direct memory access - no searching or looping required",
                "Works the same whether array has 10 or 10 million elements!"
            ],
            "complexity": "O(1) - Constant Time",
            "why_constant": "Memory access time doesn't depend on array size"
        },
        
        "Binary Search": {
            "problem": "Finding if a target value exists in a SORTED list",
            "how_it_works": [
                "Start with the middle element of the sorted list",
                "If middle = target, found it!",
                "If middle > target, search left half (eliminate right half)",
                "If middle < target, search right half (eliminate left half)",
                "Repeat until found or no elements left"
            ],
            "complexity": "O(log n) - Logarithmic Time", 
            "why_logarithmic": "Each step eliminates half the remaining possibilities"
        },
        
        "Linear Search": {
            "problem": "Finding if a target value exists in an UNSORTED list",
            "how_it_works": [
                "Start at the first element",
                "Check each element one by one: is this the target?",
                "If yes, return the position",
                "If no, move to next element",
                "Continue until found or reach end of list"
            ],
            "complexity": "O(n) - Linear Time",
            "why_linear": "In worst case, must check every single element"
        },
        
        "Find All Pairs": {
            "problem": "Finding all pairs of numbers that add up to a target sum",
            "how_it_works": [
                "Take first number, add it to every other number",
                "Take second number, add it to every remaining number", 
                "Continue for every number in the list",
                "Use nested loops: for each element, check against all others",
                "Record pairs that sum to target"
            ],
            "complexity": "O(n²) - Quadratic Time",
            "why_quadratic": "Nested loops: n × n = n² total comparisons"
        }
    }
    
    info = explanations[algorithm_name]
    
    print(f"\n" + "="*50)
    print(f"ALGORITHM DEEP DIVE: {algorithm_name.upper()}")
    print("="*50)
    
    print(f"📋 PROBLEM: {info['problem']}")
    print(f"⏰ TIME COMPLEXITY: {info['complexity']}")
    print(f"🧠 WHY THIS COMPLEXITY: {info['why_constant' if 'why_constant' in info else 'why_logarithmic' if 'why_logarithmic' in info else 'why_linear' if 'why_linear' in info else 'why_quadratic']}")
    
    print(f"\n🔧 HOW IT WORKS:")
    for i, step in enumerate(info['how_it_works'], 1):
        print(f"   {i}. {step}")
    
    print(f"\nThis algorithm should show {info['complexity'].split(' - ')[1].lower()} growth patterns.")
    input("\nPress Enter when ready to run experiments...")


def run_comparison_mode():
    """
    Allow students to compare multiple algorithms side by side.
    """
    print("\n" + "="*50)
    print("COMPARISON MODE")
    print("="*50)
    print("Compare algorithms to see how they scale differently!")
    
    algorithms = ["Array Access", "Binary Search", "Linear Search", "Find All Pairs"]
    chosen_algorithms = []
    
    print("\nChoose 2-4 algorithms to compare:")
    for i, alg in enumerate(algorithms, 1):
        choice = input(f"Include {alg}? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            chosen_algorithms.append(alg)
    
    if len(chosen_algorithms) < 2:
        print("Need at least 2 algorithms for comparison!")
        return
    
    print(f"\nComparing: {', '.join(chosen_algorithms)}")
    
    # Get input sizes
    sizes = get_input_sizes()
    
    print(f"\nRunning comparison with sizes: {sizes}")
    print("This may take a moment...")
    
    # Run experiments for all chosen algorithms
    all_results = []
    for algorithm in chosen_algorithms:
        results = run_algorithm_experiment(algorithm, sizes)
        all_results.append(results)
        print_algorithm_results(results)
    
    # Create comparison visualization
    create_comparison_plot(all_results)
    save_results_to_file(all_results, "algorithm_comparison_results.txt")
    
    print("\n" + "="*60)
    print("COMPARISON COMPLETE!")
    print("="*60)
    print("Key insights to look for:")
    print("• Array Access should stay roughly constant (flat line)")
    print("• Binary Search should grow very slowly (gentle curve)")  
    print("• Linear Search should grow proportionally (straight diagonal)")
    print("• Find All Pairs should grow rapidly (steep curve)")


def main():
    """
    Main function - orchestrates the entire activity.
    """
    try:
        # Welcome and menu
        display_algorithm_menu()
        
        # Ask if they want single algorithm study or comparison
        print("Choose your approach:")
        print("1. Study one algorithm in detail (recommended first)")
        print("2. Compare multiple algorithms side by side")
        
        while True:
            mode = input("\nEnter choice (1-2): ").strip()
            if mode in ['1', '2']:
                break
            print("Please enter 1 or 2")
        
        if mode == '1':
            # Single algorithm mode
            algorithm_name = get_algorithm_choice()
            
            print(f"\n🎉 Great choice! You've selected: {algorithm_name}")
            
            # Explain the algorithm in detail
            explain_algorithm_details(algorithm_name)
            
            # Get experiment parameters
            sizes = get_input_sizes()
            
            print(f"\nRunning {algorithm_name} experiments with sizes: {sizes}")
            print("Analyzing performance patterns...")
            
            # Run the experiment
            results = run_algorithm_experiment(algorithm_name, sizes)
            
            # Display results  
            print_algorithm_results(results)
            
            # Save results
            save_results_to_file([results], f"{algorithm_name.lower().replace(' ', '_')}_results.txt")
            
        else:
            # Comparison mode
            run_comparison_mode()
        
        # Final instructions
        print("\n" + "="*60)
        print("ACTIVITY COMPLETE! 🎉")
        print("="*60)
        print("Next Steps:")
        print("1. Review the timing patterns and ratios above")
        print("2. Complete the reflection questions in writing/reflection.md")
        print("3. Think about:")
        print("   • Which algorithm would you choose for small datasets? Large ones?")
        print("   • How do the experimental results match the theoretical complexity?")
        print("   • What real-world problems might use each algorithm?")
        print("\n📚 Don't forget to answer the reflection questions!")
        
    except KeyboardInterrupt:
        print("\n\nActivity interrupted. Run again anytime!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Make sure all files are present and try again.")


if __name__ == "__main__":
    main()