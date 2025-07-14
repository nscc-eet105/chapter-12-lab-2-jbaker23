#My name is Jacob Baker and this is Chapter 12 Lab 2 being revised on July 14
import os

def get_filename():
    while True:
        filename = input("Enter the name of the file you wish to process: ").strip()
        if os.path.isfile(filename):
            return filename
        else:
            print(f"File '{filename}' not found.")
            choice = input("Enter a new filename or type 'exit' to quit: ").strip().lower()
            filename = choice
            if choice == "exit":
                print("Thanks for using the program!")
                return None
            elif choice != (filename) or "exit":
                print(f"File '{filename}' could not be found.\nEnter a new filename or type 'exit' to quit:")
            elif choice != "":
                print("Error detected")


def count_unique_words(filename):
    unique_words = set()
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                cleaned_word = ''.join(char for char in word if char.isalnum()).lower()
                if cleaned_word:
                    unique_words.add(cleaned_word)
    return len(unique_words)

def main():
    filename = get_filename()
    if filename:
        unique_count = count_unique_words(filename)
        print(f"The file '{filename}' contains {unique_count} unique words.")

if __name__ == "__main__":
    main()
