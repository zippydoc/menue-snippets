import json
import os
import sys

def main():
    # Check if an argument is provided
    # if len(sys.argv) < 2:
        # print("Please provide the name of your Task.py file")
        # return

    # Read the input from the command line
    # input_value = sys.argv[1]

    # Strip .py
    # if input_value.endswith('.py'):
       # input_value = input_value[:-3]

	   
    # Aktuelles Verzeichnis
    # current_directory = os.getcwd()

    # Define the root of your Apple iCloud files
    current_directory = os.path.expanduser('~/Library/Mobile Documents/com~apple~CloudDocs/GitHub/menue-snippets/')


    # Define the input and output filenames
    output_filename = 'Attribute Summary.json'

    lines = read_files_in_directory(current_directory)
    write_to_file(lines, output_filename)


def write_to_file(lines, output_filename):
    try:
        # Write the stringified content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.writelines(lines)

        print(f"Successfully created {output_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_files_in_directory(directory):
    try:
        lines_with_filenames = []
        extract_lines = []
        extract_conditions = ['option', 'directory'] #ToDo: Define the condition to extract the lines

        lines_with_filenames.append("{\n")
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    #lines_with_filenames.append("{\n")
                    lines_with_filenames.append('"' + f"{file_path}"[80:] + '": ')
                    with open(file_path, 'r') as f:
                        for line in f:
                            lines_with_filenames.append(f"{line}")
                    lines_with_filenames.append(",\n")
        lines_with_filenames.append("}\n")


        #for i, line in enumerate(lines_with_filenames):
         #   for extract_condition in extract_conditions:
          #      if extract_condition in line:
           #         extract_lines.append(line)

        return lines_with_filenames

    except Exception as e:
        print(f"An error occurred: {e}")


# Function to call the main function
if __name__ == "__main__":
    main()

