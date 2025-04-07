def read_file(file_path):
    """Read the contents of a file and return them."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except IOError:
        return f"Error: An IO error occurred while reading the file '{file_path}'."


def write_file(file_path, content):
    """Write content to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return f"Successfully wrote to the file '{file_path}'."
    except IOError:
        return f"Error: An IO error occurred while writing to the file '{file_path}'."


if __name__ == "__main__":
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'

    # Read from file
    print("Reading from file:")
    read_content = read_file(input_file_path)
    print(read_content)

    # Write to file
    content_to_write = "This is a sample content."
    print("\nWriting to file:")
    write_result = write_file(output_file_path, content_to_write)
    print(write_result)

    # Read back the content from the output file
    print("\nReading back from output file:")
    read_back_content = read_file(output_file_path)
    print(read_back_content)