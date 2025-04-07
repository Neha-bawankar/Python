import shutil

# Function to copy a file
def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File copied successfully from '{source}' to '{destination}'")
    except FileNotFoundError:
        print(f"Error: The file '{source}' does not exist.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the source file and destination file
source_file = input("Enter the path of the file to copy: ")
destination_file = input("Enter the destination path for the copied file: ")

# Call the function to copy the file
copy_file(source_file, destination_file)
