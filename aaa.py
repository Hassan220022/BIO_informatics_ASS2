#!/usr/bin/python3
# Load the content of the Input.txt file to examine the sequences and prepare them for alignment
file_path_input_txt = 'Input.txt'

# Open and read the content of the file to display and check the format
with open(file_path_input_txt, 'r') as file:
    input_txt_content = file.read()

input_txt_content[:1000]  # Displaying the first 1000 characters to check the format without overloading the output