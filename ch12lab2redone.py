import os


def count_unique_words(filename):
    with open(filename, 'r') as file:
        words = set()
        for line in file:
            for word in line.split():
                cleaned_word = word.strip().lower()
                if cleaned_word:
                    words.add(cleaned_word)
        return len(words)


def main():
    print("Unique Word Counter\n")

    while True:
        filename = input("Enter the name of the file you wish to process: ")

        if os.path.isfile(filename):
            count = count_unique_words(filename)
            print(f"There are {count} unique words in {filename}.")
            break
        else:
            print(f"The file {filename} could not be found!")
            filename = input("Enter the name of the file you wish to process or type exit to quit: ")
            if filename.lower() == "exit":
                print("\nThanks for using the program!")
                return
            elif os.path.isfile(filename):
                count = count_unique_words(filename)
                print(f"There are {count} unique words in {filename}.")
                break
            else:
                print(f"The file {filename} could not be found!")
                filename = input("Enter the name of the file you wish to process or type exit to quit: ")
                if filename.lower() == "exit":
                    print("\nThanks for using the program!")
                    return

    print("\nThanks for using the program!")


if __name__ == "__main__":
    main()