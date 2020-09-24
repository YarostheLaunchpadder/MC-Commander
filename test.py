# ----- Read the file -----
# The variable filecontents is the string that contains the text
nicknamefile = open("nickname.txt", "r") # Open the file for reading
filecontents = nicknamefile.read() # Read and assign the contents to variable
nicknamefile.close() # Close the file

# Now you can assign the variable filecontents to a label to display the contanings

# ----- Write something to the file -----

nickfile = open('nickname.txt', 'w') # Open the file for writing
nickfile.write("This text will be written, it can also be a variable") # Write to the file, this will overwrite everything in the file
nickfile.close() # Close the file
