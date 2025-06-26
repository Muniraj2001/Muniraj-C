def generate_conditional_odd_series(a: int):
    result = []
    count = a if a % 2 != 0 else a - 1
    current = 1
    while len(result) < count:
        result.append(current)
        current += 2
    return result

if __name__ == "__main__":
    try:
        a = int(input("Enter a number: "))
        if a <= 0:
            print("Please enter a positive integer.")
        else:
            series = generate_conditional_odd_series(a)
            print("Output:", ", ".join(map(str, series)))
    except ValueError:
        print("Invalid input. Please enter an integer.")
