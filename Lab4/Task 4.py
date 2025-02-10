class FibonacciContainer:
    def __init__(self, n):
        self.fibonacci_sequence = self.generate_fibonacci(n)
    
    def generate_fibonacci(self, n):
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < n:
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        return fibonacci_sequence[:n]
    
    def __len__(self):
        return len(self.fibonacci_sequence)
    
    def __getitem__(self, index):
        return self.fibonacci_sequence[index]

fib_container = FibonacciContainer(10)

print(f"Довжина контейнера: {len(fib_container)}")

print("Перші 5 чисел Фібоначчі:")
for i in range(5):
    print(fib_container[i], end=" ")
