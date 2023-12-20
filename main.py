def safe_function(input_data):
    buffer_size = 10
    buffer = [""] * buffer_size
    data = input_data[:buffer_size]
    for i in range(len(data)):
        if i < buffer_size:
            buffer[i] = data[i]
    return buffer

if __name__ == "__main__":
    user_input = input("Введите строку: ")
    result = safe_function(user_input)
    print("Результат:", result)
