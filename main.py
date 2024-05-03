import pyperclip

char_to_morse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
                 "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
                 "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
                 "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
                 "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", "&": ".-...", "'": ".----.",
                 "@": ".--.-.", ")": "-.--.-", "(": "-.--.", ":": "---...", ",": "--..--", "=": "-...-",
                 "!": "-.-.--", ".": ".-.-.-", "-": "-....-", "%": "----- -..-. -----", "+": ".-.-.", '"': ".-..-.",
                 "?": "..--..", "/": "-..-.", ";": "-.-.-.", " ": "/"}


def find_key_by_value(dictionary: dict, value):
    """

    :param dictionary:
    :param value:
    Returns a dictionary key from its value.
    """
    for key, val in dictionary.items():
        if val == value:
            return key
    return None


def text_to_morse(msg: str):
    """
    :param msg:
    Takes the input text messages and encodes it to morse code.
    """

    morse_message = ""
    error_message_shown = False
    for character in msg:
        morse = char_to_morse.get(character)

        # Replaces unsupported characters with '#'
        if morse is None:
            if error_message_shown is False:
                print("Your message contains unsupported special characters. "
                      "They will be replaced with '#' in the final message.\n")
                error_message_shown = True

            morse = "#"

        morse_message += morse + " "

    morse_message = morse_message.strip()
    pyperclip.copy(morse_message)
    return morse_message


def morse_to_text(morse):
    """

    :param morse:
    Takes the inputted morse code and decodes it to readable text.
    """
    decoded_message = ""
    error_message_shown = False
    morse_list = morse.split()
    for character in morse_list:
        character_text = find_key_by_value(char_to_morse, character)

        # Replaces unsupported characters with '#'
        if character_text is None:
            if error_message_shown is False:
                print("Your message contains unsupported notation. "
                      "They will be replaced with '#' in the final message.\n")
                error_message_shown = True

            character_text = "#"

        decoded_message += character_text

    decoded_message = decoded_message.strip().lower()
    
    # To account for % notation:
    if "0/0" in decoded_message:
        decoded_message = decoded_message.replace("0/0", "%")
    pyperclip.copy(decoded_message)
    return decoded_message


while True:
    conversion_type = input("\nType 'e' to convert your text message to morse code, "
                            "while type 'd' to convert your morse code back into readable text: ").lower()

    if conversion_type == "e":
        message = input("Type the message you want to convert to morse code. "
                        "Note that only '.' and '-' notation is supported: ").upper()
        result = text_to_morse(message)

        print(f"Your morse coded message is '{result}'. \nIt has been copied to your clipboard.")

    elif conversion_type == "d":
        morse_code = input("Type the morse code you want to convert to readable text . "
                           "Note that some special characters are unsupported: ")
        result = morse_to_text(morse_code)
        print(f"Your text message is '{result}'. \nIt has been copied to your clipboard.")

    is_continue = input("Would you like to continue? Type 'y' or 'n': ").lower()
    if is_continue == "n":
        break
