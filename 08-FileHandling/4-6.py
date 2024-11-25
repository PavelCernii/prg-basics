def count_file_stats(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.readlines()

        num_lines = len(content)
        num_characters = sum(len(line) for line in content)
        num_words = sum(len(line.split()) for line in content)

        print(f"File name: {filename}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of characters: {num_characters}")
        print(f"Number of words: {num_words}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please try again.")

filename = input("Enter the file name: ")
count_file_stats(filename)
