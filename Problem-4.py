def count_multiples(numbers):
    multiples_count = {i: 0 for i in range(1, 10)}
    
    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:
                multiples_count[i] += 1

    return multiples_count

if __name__ == "__main__":
    try:
        input_str = input("Enter numbers separated by commas: ")
        number_list = [int(x.strip()) for x in input_str.split(",") if x.strip().isdigit()]
        
        if not number_list:
            print("No valid numbers entered.")
        else:
            result = count_multiples(number_list)
            print("Output:")
            print(result)
    except Exception as e:
        print("Error:", e)
