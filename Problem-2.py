def generate_odd_series(n: int):
    result = []
    current = 1
    for _ in range(n):
        result.append(current)
        current += 2
    return result

if __name__ == "__main__":
    try:
        a = int(input("Enter a number: "))
        if a <= 0:
            print("Please enter a positive integer.")
        else:
            series = generate_odd_series(a)
            print("Output:", ", ".join(map(str, series)))
    except ValueError:
        print("Invalid input. Please enter an integer.")
