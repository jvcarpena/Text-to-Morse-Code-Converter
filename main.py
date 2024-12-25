from dictionary import BOOK

# CONSTANTS
MINOR_SPACE = "   "
MAJOR_SPACE = "          "
TWIN_SPACE = " "
WELCOME_MESSAGE = '''
    +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+
    |M|o|r|s|e| |C|o|d|e| |E|n|c|o|d|e|r|
    +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+
    '''

GOODBYE_MESSAGE = '''
    +-+-+-+-+-+-+-+
    |G|o|o|d|B|y|e|
    +-+-+-+-+-+-+-+
    '''


def get_morse(word):
    """This function get the word and convert it into
    list of morse code
    :word: user input
    :result: list of morse code"""

    encoded_letters = []
    previous_letter = None

    for character in word:
        if character == ' ':  # Add a Major Space
            encoded_letters.append(MAJOR_SPACE)
            previous_letter = MAJOR_SPACE
            continue

        for key, value in BOOK.items():
            if character in key:
                if character == previous_letter:  # Add a Twin Space
                    encoded_letters.append(TWIN_SPACE)
                    encoded_letters.append(value)
                    previous_letter = character
                    continue

                if len(encoded_letters) == 0:  # Means it is the first iteration, no need to add space
                    encoded_letters.append(value)
                    previous_letter = character
                    continue

                elif previous_letter == MAJOR_SPACE:  # No need to add a MINOR SPACE
                    encoded_letters.append(value)
                    previous_letter = character
                    continue

                else:  # Add a MINOR SPACE
                    encoded_letters.append(MINOR_SPACE)
                    encoded_letters.append(value)
                    previous_letter = character
                    continue

    return encoded_letters


def output(code):
    """Get the list of morse code and convert
    it into a string
    :code: list of morse code
    :result: morse code into string"""

    empty_string = ''
    return empty_string.join(code)


def user_input():
    """Return the word that user want to convert into morse code."""
    response = str(input('\nEnter a word you want to convert into morse code: '))
    return response


def exit_input():
    """Return 'y' or 'n', if 'y' means want to continue,
    'n' means don't want to continue"""
    response = input("\nYou want to convert another word? Please enter 'y' or 'n': ").lower()
    return response


def main():

    is_program_active = True
    print('\nWelcome to my Text to Morse Code Converter!!')
    print(WELCOME_MESSAGE)

    while is_program_active:
        user_word = user_input()
        encoded_user_word = get_morse(user_word)
        word_morse_code = output(encoded_user_word)
        print(f'\nThe result of the conversion is: {word_morse_code}')

        # Exit Part
        is_want_to_exit = False

        while not is_want_to_exit:  # True
            exit_response = exit_input()

            if exit_response == 'y':
                is_program_active = True
                break

            elif exit_response == 'n':
                is_program_active = False  # Exit the main program
                print('\nThank you for using my Text to Morse Code Converter')
                print(GOODBYE_MESSAGE)
                break

            else:
                print('Invalid input, Please try again!')
                continue


if __name__ == '__main__':
    main()
