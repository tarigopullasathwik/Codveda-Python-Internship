def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)

    except FileNotFoundError:
        return "Error: File not found."


print("\n=== Word Counter Program ===")

file_name = input("Enter the file name (with .txt extension): ")
result = count_words(file_name)

print("Word Count:", result)
