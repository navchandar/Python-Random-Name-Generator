import sys

def capitalize_first_letter(wrd):
    # Convert first letter to uppercase and append the rest of the string in lowercase
    return wrd[0].upper() + wrd[1:].lower() if wrd else ""

def main(input_filename, output_filename):
    # Open the input file in reading mode
    with open(input_filename, 'r') as data_file:
        # Open the output file in write mode
        with open(output_filename, 'w') as output_file:
            # Traverse each line in the input file
            for line in data_file:
                # Split line into words
                word_list = line.split()
                # Apply function capitalize_first_letter on each word in the current line
                word_list = [capitalize_first_letter(word) for word in word_list]
                # Write the formatted line into the output file
                output_file.write(" ".join(word_list) + "\n")

if __name__ == '__main__':
    # Check if correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_filename> <output_filename>")
    else:
        # Pass the command-line arguments to main function
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        main(input_filename, output_filename)
