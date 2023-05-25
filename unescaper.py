import sys

def replace_file_contents(file_path):
    try:
        # Read the contents of the file
        with open(file_path, 'r') as file:
            contents = file.read()

        # Perform replacements
        replacements = {
            r'\\': '\\',
            r'\/': '/',
            r'\\n': '\n',
            r'\n': '\n',
            r'\\t': '\t',
            r'\"': '"',
            r"\'": "'"
        }

        for pattern, replacement in replacements.items():
            contents = contents.replace(pattern, replacement)

        # Save the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(contents)

        print(f"Replacements completed and saved to '{file_path}'.")

    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error occurred while reading or writing the file.")

# Check if a file path is provided as an argument
if len(sys.argv) < 2:
    print("Please provide the file path as an argument.")
else:
    file_path = sys.argv[1]
    replace_file_contents(file_path)
