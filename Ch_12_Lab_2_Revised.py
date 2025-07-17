import os

print("Unique Word Counter")

def unique_words():
    while True:
        filename = input("\nEnter the name of the file you wish to process: ")

        if os.path.isfile(filename):
            break
        else:
            print(f"The file {filename} could not be found!")

            # If failure occurs on the first round
            while True:
                filename = input("Enter the name of the file you wish to process or type exit to quit: ")

                if filename.lower() == 'exit':
                    print("\nThanks for using the program!")
                    return

                if os.path.isfile(filename):
                    break
                else:
                    print(f"The file {filename} could not be found!")
            break  

    unique_words_set = set()

    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                cleaned_word = ''.join(char for char in word if char.isalnum()).lower()
                if cleaned_word:
                    unique_words_set.add(cleaned_word)

    print("\n There are", len(unique_words_set),f"unique words in {filename}.")
    print("\nThanks for using the program!")

unique_words()
