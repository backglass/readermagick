import subprocess
import sys

def get_section(file_name):
    try:
        # Execute the 'identify -verbose' command with the provided file name
        result = subprocess.run(['identify', '-verbose', file_name], capture_output=True, text=True, check=True)

        # Get the standard output as a string
        output = result.stdout

        # Find the start and end indices of the desired section
        start_marker = 'Raw profile type:'
        end_marker = 'signature:'
        raw_profile_start = output.find(start_marker)
        raw_profile_end = output.find(end_marker)

        # Extract the desired section and strip it of whitespace
        raw_profile_section = output[raw_profile_start + len(start_marker):raw_profile_end].strip()

        # Split the section into individual lines and omit the first line
        lines = raw_profile_section.split('\n')[1:]

        # Concatenate all lines into a single string and remove whitespace
        merged_lines = ''.join(lines).replace(" ", "")

        # Return the section without whitespace
        return merged_lines
    except subprocess.CalledProcessError as e:
        # If there's an error executing the command, print the error message and return None
        print("Error executing the command:", e)
        return None

def create_binary_file(from_hexadecimal, file_name, as_text=False):
    try:
        # Convert the hexadecimal string into bytes
        bytes_hex = bytes.fromhex(from_hexadecimal)

        if as_text:
            # Print the hexadecimal content as UTF-8 text
            print(bytes_hex.decode('utf-8'))
        else:
            # Write the bytes to a binary file
            with open(file_name, 'wb') as f:
                f.write(bytes_hex)
            print("Binary file created successfully:", file_name)
    except Exception as e:
        print("Error creating the binary file:", e)

if __name__ == "__main__":
    # Check if an argument is provided for the image file name
    if len(sys.argv) < 2:
        print("Usage: python script.py <image_file_name> [-v]")
        sys.exit(1)

    # Get the image file name provided as an argument
    file_name = sys.argv[1]

    # Check if the optional parameter -v is provided
    as_text = False
    if "-v" in sys.argv:
        as_text = True

    # Get the desired section from the text obtained from the command
    section = get_section(file_name)

    if section:

        # Create a binary file or print the content as UTF-8 text based on the -t parameter
        create_binary_file(section, "output.bin", as_text)
