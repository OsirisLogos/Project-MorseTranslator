from datetime import datetime

# Define the Morse Code Dictionary.
# Each letter and number is mapped to its Morse Code equivalent.
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', '!': '-.-.--'}


# Function to translate English to Morse Code.
def english_to_morse(input_text):
    morse_code = ''
    for char in input_text:
        if char != ' ':
            try:
                morse_code += MORSE_CODE_DICT[char.upper()] + ' '
            except KeyError:
                print(f"Warning: Unable to translate character '{char}'. Ignoring it.")
        else:
            morse_code += '/ '
    return morse_code


# Main loop to interact with the user.
more_translations = True
attempts = 5
first_time = True

while more_translations:

    # First Block To Detect First Timers Only
    if first_time:
        user_question = input("Do you want to translate some text to morse? Type 'yes' or 'no': ").lower()
        first_time = False
    else:
        user_question = input("Do you want to translate more text to morse? Type 'yes' or 'no': ").lower()

    # If First Time is False
    if user_question == 'yes':
        user_input = input("Write your text here: ")
        print(f"Your text in morse is: {english_to_morse(user_input)}")
    elif user_question == 'no':
        more_translations = False
        print(f"Thanks for using our services. Have a great day! \n©️LogosLabs {datetime.now().year}")
    else:
        print("I'm sorry. I can't understand what you type. Please type only 'yes' or 'no'. Thanks")
        attempts -= 1
        if attempts == 0:
            more_translations = False
            print("Try again later.")
            print(f"Thanks for using our services. Have a great day! \n©️LogosLabs {datetime.now().year}")

