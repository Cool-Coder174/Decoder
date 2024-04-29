def decode(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Initialize an empty dictionary to store the number-word pairs
    pyramid = {}

    # Process each line in the file
    for line in lines:
        # Split the line into a number and a word
        number, word = line.split()
        # Store the number-word pair in the dictionary
        pyramid[int(number)] = word

    # Initialize an empty list to store the message words
    message = []

    # Initialize the step variable to 1
    step = 1

    # While the current step is in the pyramid
    while step in pyramid:
        # Append the word corresponding to the current step to the message
        message.append(pyramid[step])
        # Increment the step by the current step (to get the next number at the end of the pyramid line)
        step += step

    # Join the message words with spaces and return the resulting string
    return ' '.join(message)

message = decode('coding_qual_input.txt')
print(message) 