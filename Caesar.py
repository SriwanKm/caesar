# coding=utf-8

# variable declaration
FINAL_ALPHABETIC_ORDINAL_PLUS_ONE = 123
INITIAL_ALPHABETIC_ORDINAL = 97
WHITESPACE_ORDINAL = 32
SHIFT = 3
WHITESPACE = " "


def validate_input(text):
    words = input(text)
    while not words.islower() or not words.replace(" ", "").isalpha():
        words = input("Please use all lowercase alphabetic characters: ")
    return words


def to_encode():
    e = validate_input("What's the text you want to encode: ")

    # mapping the input(e) and feed each letter into the function encode_letter
    # the result of function encode_letter come out in the form of an object so we turn it back into array using list()
    # then join the array to get string format
    print("Your encoded text is:", "".join(list(map(encode_letter, e))))


def to_decode():
    d = validate_input("What's the text you want to decode: ")

    # mapping the input(d) and feed each letter into the function decode_letter
    # the result of function decode_letter come out in the form of an object so we turn it back into array using list()
    # then join the array to get string format
    print("Your decoded text is:", "".join(list(map(decode_letter, d))))


def encode_letter(letter):
    new_letter = ord(letter) + SHIFT
    # get ordinal number of the letter and shift up 3

    if letter == WHITESPACE:
        new_letter = WHITESPACE_ORDINAL
        # if the letter is a whitespace remain the same

    elif new_letter >= FINAL_ALPHABETIC_ORDINAL_PLUS_ONE:
        new_letter = new_letter % FINAL_ALPHABETIC_ORDINAL_PLUS_ONE + INITIAL_ALPHABETIC_ORDINAL
        # after shifting if the order number over the letter "z" then using mod to start with letter "a" again

    return chr(new_letter)


def decode_letter(letter):
    new_letter = ord(letter) - SHIFT
    # get ordinal number of the letter and shift down 3

    if letter == WHITESPACE:
        new_letter = WHITESPACE_ORDINAL
        # if the letter is a whitespace remain the same

    elif new_letter < INITIAL_ALPHABETIC_ORDINAL:
        new_letter = FINAL_ALPHABETIC_ORDINAL_PLUS_ONE - INITIAL_ALPHABETIC_ORDINAL % new_letter
        # after shifting if the ordinal number less than the letter "a" then using mod to start from "z"

    return chr(new_letter)


print("""
╭╮╭╮╭┳━━━┳╮╱╱╭━━━┳━━━┳━╮╭━┳━━━╮
┃┃┃┃┃┃╭━━┫┃╱╱┃╭━╮┃╭━╮┃┃╰╯┃┃╭━━╯
┃┃┃┃┃┃╰━━┫┃╱╱┃┃╱╰┫┃╱┃┃╭╮╭╮┃╰━━╮
┃╰╯╰╯┃╭━━┫┃╱╭┫┃╱╭┫┃╱┃┃┃┃┃┃┃╭━━╯
╰╮╭╮╭┫╰━━┫╰━╯┃╰━╯┃╰━╯┃┃┃┃┃┃╰━━╮
╱╰╯╰╯╰━━━┻━━━┻━━━┻━━━┻╯╰╯╰┻━━━╯""")

while True:
    start = input("To start the program type e to encode, d to decode, or q to quit: ")
    if start == "q":
        print("""
███████████████████████████████████████
█▄─▄─▀█▄─█─▄█▄─▄▄─███▄─▄─▀█▄─█─▄█▄─▄▄─█
██─▄─▀██▄─▄███─▄█▀████─▄─▀██▄─▄███─▄█▀█
▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀""")

    elif start == "e":
        to_encode()

    elif start == "d":
        to_decode()


# oryh ph olnh brx vdb
