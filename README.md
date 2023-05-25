# Unescaper

This is a Python script that replaces specific patterns in a text file with their corresponding replacements. It takes a file path as an argument and performs the replacements on the contents of the file. The modified content is then saved back to the file.

The script first reads the contents of the file specified by the provided file path. It then defines a dictionary called replacements which maps patterns to their corresponding replacements. These patterns include escape sequences and special characters commonly found in text files.

The script iterates over each key-value pair in the replacements dictionary and uses the replace() method to substitute the patterns with their replacements in the file contents.

After performing the replacements, the modified content is saved back to the file, overwriting the original content. Finally, a message is printed indicating that the replacements have been completed and the file has been saved.

If the specified file path is invalid or the file cannot be read or written, appropriate error messages are displayed.

It can unescape any file-type like: html, json, yaml etc...

## Usage

Clone the repository:

    git clone https://github.com/josemlwdf/unescaper.git

Navigate to the script's directory:

    cd unescaper

Run the script with the file path as an argument:

    python unescaper.py /path/to/file.txt

Make sure to replace /path/to/file.txt with the actual path to the file you want to modify.

The script will perform the replacements on the file contents and save the modified content back to the file. If the file path is invalid or there are issues with reading or writing the file, appropriate error messages will be displayed.

## Notes

This script requires Python 3.
The file to be modified should be a text file.
The script replaces specific patterns defined in the replacements dictionary. You can modify the dictionary to add or customize patterns and replacements according to your needs.
