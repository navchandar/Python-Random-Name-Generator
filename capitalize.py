def capitalize_first_letter(wrd):
    # convert first letter to upper and 
    # append the rest of the string to it
    return wrd[0].upper() + wrd[1:].lower()
 
# open data.txt file in reading mode
with open('healthcare-and-medical-jobs.txt', 'r') as data_file:
   
    # open output.txt file in append mode
    with open('output.txt', 'a') as output_file:
       
        # traverse each line in data.txt file
        for line in data_file:
           
            # split line into words
            word_list = line.split()
             
            # apply function capitalize_first_letter 
            # on each word in current line
            word_list = [capitalize_first_letter(word) for word in word_list]
             
            # write the line into output.txt file after 
            # capitalizing the first letter in a word 
            # in the current line
            output_file.write(" ".join(word_list) + "\n")