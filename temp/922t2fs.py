# Generate the first 50 Fibonacci numbers and calculate their sum

def generate_fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

def main():
    count = 50
    fibonacci_sequence = generate_fibonacci(count)
    total_sum = sum(fibonacci_sequence)
    
    print("First 50 Fibonacci numbers:")
    print(fibonacci_sequence)
    print("\nSum of the first 50 Fibonacci numbers:")
    print(total_sum)

main()
