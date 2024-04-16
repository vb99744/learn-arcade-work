import re

# this function takes in a line of text and returns
# a list of words in the line
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():
    """ Read lines from a file """

    # open dictionary file
    dictionary_file = open("dictionary.txt")

    # create an empty list to store the words
    dictionary_list = []

    # loop through each line in the file like a list
    for line in dictionary_file:
            line = line.strip()
            dictionary_list.append(line)
    dictionary_file.close()

    # add the linear search of the alice text
    print("--- Linear Search ---")
    alice_file = open("AliceInWonderLand200.txt")

    # start at the beginning of the list
    line_number = 0

    # loop through each line to make a list
    for line in alice_file:
        # remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()
        word_list = split_line(line)
        line_number += 1

        # loop through each word in the list
        for word in word_list:
            # restart at the beginning of the list
            current_line_number = 0
            # loop until you reach the end of the list, or the value at the
            # current position is equal to the key (word.upper())
            while current_line_number < len(dictionary_list) and dictionary_list[current_line_number] != word.upper():
                # go to the next item on the list
                current_line_number += 1

            if current_line_number < len(dictionary_list):
                continue
            else:
                print(f"Line {line_number} possible misspelled word: {word}")

    alice_file.close()

    # start the binary search of the alice text
    print("--- Binary Search ---")

    alice_file = open("AliceInWonderLand200.txt")
    # start from the beginning of the list
    line_number = 0

    for line in alice_file:
        line_number += 1
        line = line.strip()
        word_list = split_line(line)

        for word in word_list:
            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False

            # Loop until we find the item, or our upper/lower bounds meet
            while lower_bound <= upper_bound and not found:

                # Find the middle position
                middle_pos = (lower_bound + upper_bound) // 2

                # Figure out if we:
                # move up the lower bound, or
                # move down the upper bound, or
                # we found what we are looking for

                if dictionary_list[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > key:
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print(f"Line {line_number} possible misspelled word: {word}")

    alice_file.close()

main()