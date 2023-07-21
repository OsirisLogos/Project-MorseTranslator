English to Morse Code Translator

This Python script translates English text into Morse code.
Features

    Translates both letters and numbers, as well as some common punctuation marks.
    Allows multiple translations in a single session.
    Provides clear error messages for invalid inputs.
    Limits the number of invalid attempts to prevent endless loops.

Usage

    Run the script: python main.py
    When asked "Do you want to translate some text to morse? Type 'yes' or 'no':", type 'yes' to start a translation, or 'no' to exit.
    If you chose 'yes', you will be asked to input the text you want to translate. Type your text and press Enter.
    The translated Morse code will be printed to the console.
    You will be asked if you want to translate more text. If you type 'yes', the process will repeat. If you type 'no', the script will exit.
    If you input anything other than 'yes' or 'no' when asked if you want to translate more text, you will receive an error message and the number of remaining attempts will decrease. If you make 5 invalid attempts, the script will automatically exit.

Limitations

    The script only translates characters that are included in the Morse code dictionary. If the input text includes other characters, a warning message will be printed and the character will be ignored.

License

This project is licensed under the MIT License.