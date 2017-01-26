def alphabet_position(letter):
    """
    Takes a character and adjusts the ordinal to be 0 - 25.
    This number is then mod 26 to allow later letters in the alphabet to wrap back to the
    beginning of the alphabet.
    """
    oldLetterOrd = ord(letter)
    if letter.isupper():
        adjLetterOrd = oldLetterOrd - 65
    else:
        adjLetterOrd = oldLetterOrd - 97

    return adjLetterOrd

def rotate_character(char, rot):
    """ A character is received.  If it is alphabetic, it is rotated and returned.
        If it is not alphabetic, the character is returned as-is
    """

    newCharOrd = alphabet_position(char)
    adjCharOrd = (newCharOrd + int(rot)) % 26

    if char.isalpha():
        if char.isupper():            # add in uppercase ASCII offset
            adjCharOrd = adjCharOrd + int(65)
        else:                         # add in lowercase ASCII offset
            adjCharOrd = adjCharOrd + int(97)
        newChar = chr(adjCharOrd)
    else:                             # get non alphabetic characters ready to return
        newChar = char

    return newChar

def encrypt(text,rot):
    """
    step through the message character by character.  Each alphabetic character is
    then processed through charEncrypt and the encrypted message is reassembled.
    """
    newMess = ""
    for char in text:
        newChar = rotate_character(char, rot)
        newMess = newMess + newChar

    return newMess
