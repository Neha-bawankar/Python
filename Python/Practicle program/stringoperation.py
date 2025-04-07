class StringOperations:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_string(self):
        """Return the reversed string."""
        return self.input_string[::-1]

    def is_palindrome(self):
        """Check if the string is a palindrome."""
        reversed_string = self.reverse_string()
        return self.input_string == reversed_string

    def find_substring(self, substring):
        """Find the index of the first occurrence of a substring."""
        return self.input_string.find(substring)

    def to_upper_case(self):
        """Convert the string to upper case."""
        return self.input_string.upper()

    def to_lower_case(self):
        """Convert the string to lower case."""
        return self.input_string.lower()

    def capitalize_string(self):
        """Capitalize the first character of the string."""
        return self.input_string.capitalize()

    def title_case_string(self):
        """Convert the string to title case."""
        return self.input_string.title()

    def count_occurrences(self, substring):
        """Count the occurrences of a substring in the string."""
        return self.input_string.count(substring)

    def replace_substring(self, old_substring, new_substring):
        """Replace all occurrences of a substring with a new substring."""
        return self.input_string.replace(old_substring, new_substring)

    def split_string(self, delimiter=" "):
        """Split the string into a list of substrings based on a delimiter."""
        return self.input_string.split(delimiter)

    def join_strings(self, list_of_strings, delimiter=" "):
        """Join a list of strings into a single string with a delimiter."""
        return delimiter.join(list_of_strings)


if __name__ == "__main__":
    input_str = "Hello, Python String Operations!"
    string_operations = StringOperations(input_str)

    print("Original String:", string_operations.input_string)
    print("Reversed String:", string_operations.reverse_string())
    print("Is Palindrome:", string_operations.is_palindrome())
    print("Find 'Python':", string_operations.find_substring("Python"))
    print("To Upper Case:", string_operations.to_upper_case())
    print("To Lower Case:", string_operations.to_lower_case())
    print("Capitalize String:", string_operations.capitalize_string())
    print("Title Case String:", string_operations.title_case_string())
    print("Count 'string':", string_operations.count_occurrences("string"))
    print("Replace 'string' with 'text':", string_operations.replace_substring("string", "text"))
    print("Split String:", string_operations.split_string())
    print("Join Strings:", string_operations.join_strings(['Join', 'these', 'words'], delimiter="-"))