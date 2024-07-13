def process_data(input_data):
    processed_data = input_data.upper()
    return processed_data

if __name__ == "__main__":
    data = "Amirreza Razazian - Filoger MLOPS Class!"
    result = process_data(data)
    print(result)
