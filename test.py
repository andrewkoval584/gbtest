def filter_strings(input_array):
    filtered_array = []
    
    for string in input_array:
        if len(string) <= 3:
            filtered_array.append(string)
    return filtered_array

def main():
    n = int(input("Введите количество строк в массиве: "))
    
    input_array = []
    
    for i in range(n):
        string = input(f"Введите строку {i + 1}: ")
        input_array.append(string)
    
    filtered_array = filter_strings(input_array)
    print(filtered_array)

if __name__ == "__main__":
    main()